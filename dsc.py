#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import sys
import datetime
from endesive import pdf, hsm
 
import os
import sys
 
if sys.platform == 'win32':
    dllpath = r'c:\windows\system32\cryptoCertum3PKCS.dll'
else:
    dllpath = '/usr/lib/WatchData/ProxKey/lib/libwdpkcs_SignatureP11.so'
 
import PyKCS11 as PK11
 
class Signer(hsm.HSM):
    def certificate(self):
        #print(self.pkcs11.getSlotList(tokenPresent=True))
        #print(self.pkcs11.getTokenInfo(1))
#        print(self.pkcs11.getTokenInfo(2))
#        print(self.pkcs11.getTokenInfo(3))
 
 
#        print(self.pkcs11.getSlotInfo(1))
        self.login("WD PROXKey","12345678") # WF PROXKey is token name.
        keyid = [0x5e, 0x9a, 0x33, 0x44, 0x8b, 0xc3, 0xa1, 0x35, 0x33, 0xc7, 0xc2, 0x02, 0xf6, 0x9b, 0xde, 0x55, 0xfe, 0x83, 0x7b, 0xde]
        #keyid = [0x3f, 0xa6, 0x63, 0xdb, 0x75, 0x97, 0x5d, 0xa6, 0xb0, 0x32, 0xef, 0x2d, 0xdc, 0xc4, 0x8d, 0xe8]
        keyid = bytes(keyid)
        try:
            pk11objects = self.session.findObjects([(PK11.CKA_CLASS, PK11.CKO_CERTIFICATE)])
            all_attributes = [
                #PK11.CKA_SUBJECT,
                PK11.CKA_VALUE,
                #PK11.CKA_ISSUER,
                #PK11.CKA_CERTIFICATE_CATEGORY,
                #PK11.CKA_END_DATE,
                PK11.CKA_ID,
            ]
 
            for pk11object in pk11objects:
                try:
                    attributes = self.session.getAttributeValue(pk11object, all_attributes)
                except PK11.PyKCS11Error as e:
                    continue
 
                attrDict = dict(list(zip(all_attributes, attributes)))
                cert = bytes(attrDict[PK11.CKA_VALUE])
                #if keyid == bytes(attrDict[PK11.CKA_ID]):
                return bytes(attrDict[PK11.CKA_ID]), cert
        finally:
            self.logout()
        return None, None
 
    def sign(self, keyid, data, mech):
        self.login("WD PROXKey","12345678")
        try:
            privKey = self.session.findObjects([(PK11.CKA_CLASS, PK11.CKO_PRIVATE_KEY)])[0]
            mech = getattr(PK11, 'CKM_%s_RSA_PKCS' % mech.upper())
            sig = self.session.sign(privKey, data, PK11.Mechanism(mech, None))
            return bytes(sig)
        finally:
            self.logout()
 
def main():
    date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
    date = date.strftime('%Y%m%d%H%M%S+00\'00\'')
    dct = {
        "sigflags": 3,
        "sigpage": 0,
        "sigbutton": True,
        "contact": "madhurendra@tikaj.com",
        "location": 'India',
        "signingdate": date.encode(),
        "reason": 'Sample sign',
        "signature": 'Madhurendra Sachan',
        "signaturebox": (0, 0, 100, 100),
    }
    clshsm = Signer(dllpath)
    fname = 'sample.pdf'
    datau = open(fname, 'rb').read()
    datas = pdf.cms.sign(datau, dct,
        None, None,
        [],
        'sha256',
        clshsm,
    )
    fname = fname.replace('.pdf', '-signed.pdf')
    with open(fname, 'wb') as fp:
        fp.write(datau)
        fp.write(datas)
 
 
main()