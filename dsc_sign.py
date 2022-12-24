# Importing the PIL library
import sys
from lib import img,pdf,dsc,utl
inp_data = sys.argv[1]
print(inp_data)
inp_data = inp_data.split(",")
img.set_image(inp_data)
pdf.add_stamp(inp_data)
dsc.set_dsign(inp_data)
utl.del_xfile(inp_data)
