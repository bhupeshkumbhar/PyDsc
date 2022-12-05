import sys
import datetime
from endesive.pdf        import cms
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12

def set_dsign(inp_data):
    inp_file = inp_data[0]
    out_file = inp_file.replace("_inp","_out")
    dsc_file = out_file.replace("inp/","out/")
    dsc_file = dsc_file.replace("_out","_signed")
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
        dsc_cert = pkcs12.load_key_and_certificates(
            fp.read(), b"12345678", backends.default_backend()
        )

    out_data = open(out_file, "rb").read()
    dsc_data = cms.sign(out_data, dct, dsc_cert[0], dsc_cert[1], dsc_cert[2], "sha256")

    with open(dsc_file, "wb") as fp:
        fp.write(out_data)
        fp.write(dsc_data)