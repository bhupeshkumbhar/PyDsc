import json,datetime,base64
from PIL                        import Image
from PIL                        import ImageDraw
from PIL                        import ImageFont
from digital_certificate.cert   import Certificate

def set_image(inp_data):
    cfg_file = open('cfg/config.json')
    cfg_json = json.load(cfg_file)
    dsc_ccod = inp_data[3]
    dsc_path = cfg_json["DSC_CERT_LIST"][dsc_ccod]["DSC_CERT_PATH"]
    dsc_pswd = cfg_json["DSC_CERT_LIST"][dsc_ccod]["DSC_CERT_PSWD"]
    dsc_pswd = base64.b64decode(dsc_pswd)

    dsc_cert = Certificate(
        pfx_file=dsc_path,
        password=dsc_pswd
    )
    dsc_cert.read_pfx_file()
    # Open an Image
    img_file = Image.open('cfg/dsc_inp.png')
    
    # Call draw Method to add 2D graphics in an image
    img_data = ImageDraw.Draw(img_file)
    
    # Custom font style and font size
    txt_font = ImageFont.truetype("arialbd.ttf", 9, encoding="unic")
    dsc_name = dsc_cert.common_name()
    dsc_name = dsc_name.replace('DS ','')
    dsc_appr = inp_data[4]
    cur_date = datetime.datetime.now()
    dsc_date = cur_date.strftime("%Y-%m-%d %H:%M:%S")

    # Add Text to an image
    img_data.text((10, 10), "Digitally Signed By",    font=txt_font,  fill =(105, 105, 105))
    img_data.text((10, 20), dsc_name,                 font=txt_font,  fill =(105, 105, 105))
    img_data.text((10, 30), "Date : "   + dsc_date,   font=txt_font,  fill =(105, 105, 105))
    img_data.text((10, 40), "Appr By : "+ dsc_appr,   font=txt_font,  fill =(105, 105, 105))
    
    # Save the edited image
    img_file.save("cfg/dsc_out.png")

