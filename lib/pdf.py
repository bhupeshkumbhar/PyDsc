import os,json
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

def add_stamp(inp_data):
    inp_file = inp_data[0]
    dsc_outp = inp_data[2]
    cfg_file = open('cfg/config.json')
    cfg_json = json.load(cfg_file)
    dsc_cord = cfg_json["DSC_OUTP_LIST"][dsc_outp]
    img_file = inp_file.replace("_inp","_img")

    inp_canv = canvas.Canvas(img_file)
    inp_canv.drawImage('cfg/dsc_out.png', dsc_cord[1], dsc_cord[2])
    inp_canv.save()
    
    img_file = PdfFileReader(open(img_file, "rb"))
    pdf_read = PdfFileReader(open(inp_file, "rb"))
    pdf_writ = PdfFileWriter()
    out_file = inp_file.replace("_inp","_out")
    pdf_pcnt = pdf_read.getNumPages()
    
    for pdf_page in range(pdf_pcnt):
        # merge the watermark with the page
        inp_page = pdf_read.getPage(pdf_page)
        inp_page.mergePage(img_file.getPage(0))
        pdf_writ.addPage(inp_page)
    
    with open(out_file, "wb") as outputStream:
        pdf_writ.write(outputStream)

def view_xpdf(inp_data):
    inp_file = inp_data[0]
    dsc_file = inp_file.replace("inp/","out/")
    dsc_file = dsc_file.replace("_inp","_signed")
    dsc_file = os.path.abspath(dsc_file)
    os.system(dsc_file)

