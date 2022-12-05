import json,datetime,base64
from PIL                        import Image
from PIL                        import ImageDraw
from PIL                        import ImageFont
from digital_certificate.cert   import Certificate

def set_image():

    file = open('cfg/config.json')
    config = json.load(file)

    dsc_path = config["DSC_CERT_LIST"]["1100"]["DSC_CERT_PATH"]
    dsc_pswd = config["DSC_CERT_LIST"]["1100"]["DSC_CERT_PSWD"]
    dsc_pswd = base64.b64decode(dsc_pswd)

    cert = Certificate(
        pfx_file=dsc_path,
        password=dsc_pswd
    )
    cert.read_pfx_file()
    # Open an Image
    img = Image.open('cfg/dsc_inp.png')
    
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    # Custom font style and font size
    myFont = ImageFont.truetype("arialbd.ttf", 9, encoding="unic")
    dsc_name = cert.common_name()
    dsc_name = dsc_name.replace('DS ','')
    dsc_appr = 'Bhupesh Kumbhar'
    cur_date = datetime.datetime.now()
    dsc_date = cur_date.strftime("%Y-%m-%d %H:%M:%S")

    # Add Text to an image
    I1.text((10, 10), "Digitally Signed By",    font=myFont,  fill =(105, 105, 105))
    I1.text((10, 20), dsc_name,                 font=myFont,  fill =(105, 105, 105))
    I1.text((10, 30), "Date : "   + dsc_date,   font=myFont,  fill =(105, 105, 105))
    I1.text((10, 40), "Appr By : "+ dsc_appr,   font=myFont,  fill =(105, 105, 105))
    
    # Display edited image
    #img.show()
    
    # Save the edited image
    img.save("cfg/dsc_out.png")

