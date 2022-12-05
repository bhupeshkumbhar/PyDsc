import sys
import datetime
from endesive.pdf        import cms
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12

def set_dsign():
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
        "signaturebox": (370, 16, 550, 80),
        "signature": "",
        "signature_img": "",
        "contact": "",
        "location": "",
        "signingdate": date,
        "reason": "Digital Sign",
        "password": "Test@123",
    }
    with open("cfg/dsc_1100.pfx", "rb") as fp:
        p12 = pkcs12.load_key_and_certificates(
            fp.read(), b"12345678", backends.default_backend()
        )

    fname = "inp/9100602265_ZBAL_00_out.pdf"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    datau = open(fname, "rb").read()
    datas = cms.sign(datau, dct, p12[0], p12[1], p12[2], "sha256")
    fname = fname.replace("inp/", "out/")
    fname = fname.replace("_out.pdf", "_signed.pdf")
    with open(fname, "wb") as fp:
        fp.write(datau)
        fp.write(datas)