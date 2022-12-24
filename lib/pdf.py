import os,json
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader,PdfWriter

def add_stamp(inp_data):
    inp_path = inp_data[0]
    dsc_outp = inp_data[2]
    with open('cfg/config.json') as cfg_file:
        cfg_json = json.load(cfg_file)
    dsc_cord = cfg_json["DSC_OUTP_LIST"][dsc_outp]
    img_path = inp_path.replace("_inp","_img")

    inp_canv = canvas.Canvas(img_path)
    inp_canv.drawImage('cfg/dsc_out.png', dsc_cord[1], dsc_cord[2])
    inp_canv.save()
    img_file = open(img_path, "rb")
    inp_file = open(inp_path, "rb")
    img_cont = PdfReader(img_file)
    inp_cont = PdfReader(inp_file)
    pdf_writ = PdfWriter()
    out_path = inp_path.replace("_inp","_out")
    pdf_pcnt = len(inp_cont.pages)
    for pdf_page in range(pdf_pcnt):
        # merge the watermark with the page
        inp_page = inp_cont.pages[pdf_page]
        inp_page.merge_page(img_cont.pages[0])
        pdf_writ.add_page(inp_page)
    
    with open(out_path, "wb") as outputStream:
        pdf_writ.write(outputStream)
    
    inp_file.close()
    img_file.close()

def view_xpdf(inp_data):
    inp_path = inp_data[0]
    dsc_path = inp_path.replace("_inp","_signed")
    dsc_path = dsc_path.replace("inp\\","out\\")
    
    dsc_path = os.path.abspath(dsc_path)
    os.system(dsc_path)

