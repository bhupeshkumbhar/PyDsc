import sys,json,base64
import datetime
from endesive.pdf        import cms
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12

def set_dsign(inp_data):
    cfg_file = open('cfg/config.json')
    cfg_json = json.load(cfg_file)
    inp_file = inp_data[0]
    dsc_date = inp_data[1]
    dsc_outp = inp_data[2]
    dsc_ccod = inp_data[3]
    dsc_cord = cfg_json["DSC_OUTP_LIST"][dsc_outp]
    print(dsc_cord[1])
    img_file = inp_file.replace("_inp","_img")
    out_file = inp_file.replace("_inp","_out")
    dsc_file = out_file.replace("inp/","out/")
    dsc_file = dsc_file.replace("_out","_signed")
    dsc_path = cfg_json["DSC_CERT_LIST"][dsc_ccod]["DSC_CERT_PATH"]
    dsc_pswd = cfg_json["DSC_CERT_LIST"][dsc_ccod]["DSC_CERT_PSWD"]
    dsc_pswd = base64.b64decode(dsc_pswd)
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
        "signaturebox": (dsc_cord[1],dsc_cord[2],dsc_cord[3],dsc_cord[4]), #(370, 16, 550, 80),
        "signature": "",
        "signature_img": "",
        "contact": "",
        "location": "",
        "signingdate": date,
        "reason": "Digital Sign",
        "password": "Test@123",
    }

    with open(dsc_path, "rb") as fp:
        dsc_cert = pkcs12.load_key_and_certificates(
            fp.read(), dsc_pswd, backends.default_backend()
        )

    out_data = open(out_file, "rb").read()
    dsc_data = cms.sign(out_data, dct, dsc_cert[0], dsc_cert[1], dsc_cert[2], "sha256")

    with open(dsc_file, "wb") as fp:
        fp.write(out_data)
        fp.write(dsc_data)