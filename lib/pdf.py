import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

def add_stamp():
    c = canvas.Canvas('inp/9100602265_ZBAL_00_img.pdf')
    c.drawImage('cfg/dsc_out.png', 370, 16)
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

def view_xpdf():
    os.system("D:\Projects\pyDsc\out\9100602265_ZBAL_00_signed.pdf")

