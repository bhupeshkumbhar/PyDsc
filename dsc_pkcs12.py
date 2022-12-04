#https://github.com/m32/endesive/blob/master/examples/pdf-sign-cms.py
#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import sys
import datetime
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12

from endesive.pdf import cms

# from endesive.pdf import cmsn as cms

# import logging
# logging.basicConfig(level=logging.DEBUG)


def main():
    date = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
    date = date.strftime("D:%Y%m%d%H%M%S+00'00'")
    dct = {
        "aligned": 0,
        "sigflags": 3,
        "sigflagsft": 132,
        "sigpage": 0,
        "sigbutton": True,
        "sigfield": "Signature1",
        "auto_sigfield": True,
        "sigandcertify": True,
        "signaturebox": (350, 30, 550, 80),
        "signature": "",
        "signature_img": "signature_test.png",
        "contact": "bhupesh.kumbhar@zencon.co.in",
        "location": "Pune",
        "signingdate": date,
        "reason": "Digital Sign",
        "password": "Test@123",
    }
    with open("dsc_1100.pfx", "rb") as fp:
        p12 = pkcs12.load_key_and_certificates(
            fp.read(), b"Test@123", backends.default_backend()
        )

    
    
    fname = "document-output.pdf"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    datau = open(fname, "rb").read()
    datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
    fname = fname.replace(".pdf", "-signed-cms.pdf")
    with open(fname, "wb") as fp:
        fp.write(datau)
        fp.write(datas)

main()