# Importing the PIL library
import sys
from lib import img,pdf,dsc,utl
inp_data = sys.argv[1]
inp_data = inp_data.split(",")
inp_file = inp_data[0]
out_file = inp_file.replace("_inp","_out")
dsc_file = out_file.replace("inp/","out/")
dsc_file = dsc_file.replace("_out","_signed")
img.set_image(inp_data)
pdf.add_stamp(inp_data)
dsc.set_dsign(inp_data)
pdf.view_xpdf(inp_data)
#utl.delete(inp_file)
