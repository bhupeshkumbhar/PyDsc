# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
# Open an Image
img = Image.open('dsc.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Custom font style and font size
myFont = ImageFont.truetype("arialbd.ttf", 9, encoding="unic")

# Add Text to an image
I1.text((10, 10), "Digitally Signed By",        font=myFont,  fill =(105, 105, 105))
I1.text((10, 20), "UMASONS AUTOCOMP PVT LTD",   font=myFont,  fill =(105, 105, 105))
I1.text((10, 30), "Date : 2022-12-04 17:50:00", font=myFont,  fill =(105, 105, 105))
I1.text((10, 40), "Appr By : Bhupesh Kumbhar",  font=myFont,  fill =(105, 105, 105))
 
# Display edited image
img.show()
 
# Save the edited image
img.save("dsc_signed.png")