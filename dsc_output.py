from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

c = canvas.Canvas('dsc_image.pdf')
c.drawImage('dsc_signed.png', 370, 16)
#c.drawString(350, 50,"Hello World")
c.save()

dsc_image = PdfFileReader(open("dsc_image.pdf", "rb"))
output_file = PdfFileWriter()
input_file = PdfFileReader(open("inv_copy.pdf", "rb"))
page_count = input_file.getNumPages()


for page_number in range(page_count):
    # merge the watermark with the page
    input_page = input_file.getPage(page_number)
    input_page.mergePage(dsc_image.getPage(0))
    # add page from input file to output document
    output_file.addPage(input_page)

with open("document-output.pdf", "wb") as outputStream:
    output_file.write(outputStream)