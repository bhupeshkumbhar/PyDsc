# Importing the PIL library
import os,sys,json,datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from endesive.pdf        import cms
from reportlab.pdfgen    import canvas
from cryptography.hazmat import backends
from PyPDF2 import PdfFileWriter, PdfFileReader
from digital_certificate.cert import Certificate
from cryptography.hazmat.primitives.serialization import pkcs12


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
            fp.read(), b"Test@123", backends.default_backend()
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

file = open('cfg/config.json')
config = json.load(file)

cert = Certificate(
    pfx_file="cfg/dsc_1100.pfx",
    password=b"Test@123"
)
cert.read_pfx_file()
# Open an Image
img = Image.open('cfg/dsc_inp.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Custom font style and font size
myFont = ImageFont.truetype("arialbd.ttf", 9, encoding="unic")
dsc_name = cert.common_name()
dsc_appr = 'Bhupesh Kumbhar'
cur_date = datetime.datetime.now()
dsc_date = cur_date.strftime("%Y-%m-%d %H:%M:%S")

# Add Text to an image
I1.text((10, 10), "Digitally Signed By",        font=myFont,  fill =(105, 105, 105))
I1.text((10, 20), dsc_name,   font=myFont,  fill =(105, 105, 105))
I1.text((10, 30), "Date : "   + dsc_date, font=myFont,  fill =(105, 105, 105))
I1.text((10, 40), "Appr By : "+ dsc_appr, font=myFont,  fill =(105, 105, 105))
 
# Display edited image
#img.show()
 
# Save the edited image
img.save("cfg/dsc_out.png")

c = canvas.Canvas('inp/9100602265_ZBAL_00_img.pdf')
c.drawImage('cfg/dsc_out.png', 370, 16)
#c.drawString(350, 50,"Hello World")
c.save()

dsc_image = PdfFileReader(open("inp/9100602265_ZBAL_00_img.pdf", "rb"))
output_file = PdfFileWriter()
input_file = PdfFileReader(open("inp/9100602265_ZBAL_00_inp.pdf", "rb"))
page_count = input_file.getNumPages()


for page_number in range(page_count):
    # merge the watermark with the page
    input_page = input_file.getPage(page_number)
    input_page.mergePage(dsc_image.getPage(0))
    # add page from input file to output document
    output_file.addPage(input_page)

with open("inp/9100602265_ZBAL_00_out.pdf", "wb") as outputStream:
    output_file.write(outputStream)

main()
os.system("D:\Projects\pyDsc\out\9100602265_ZBAL_00_signed.pdf")
