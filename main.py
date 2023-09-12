# The program requires pillow
# python -m pip install pillow
from PIL import Image
import math
print("Start")

# import Image from PIL
# use Image.open to open the file and assign it to a variable
# load the image with <reference>.load and store the pixel buffer
# Get the width and height by getting the first and second array entries of <reference>.size
# loop over y and x
# get the pixel at <buffer>[x,y]
# get the rgb of <pixel> by accessing array values 0,1,2
# create a new list of (r,g,b)
# update <buffer>[x,y] with the new list
# save <reference> with <reference>.save("filename.ext", "ext"


image = Image.open("bridge.jpg")
buffer = image.load()
width = image.size[0]
height = image.size[1]

container = Image.new("RGB", (width*2,height*2))
c_buffer = container.load()


for y in range(height):
    for x in range(width):
        pixel = buffer[x, y]

        # keep the original color
        r, g, b = pixel
        c_buffer[x, y] = (r,g,b)

        #grayscale
        gray = max(pixel)
        c_buffer[x+width,y] = (gray, gray, gray)

        gray2 = math.floor((r + g + b)/3)
        c_buffer[x,y+height] = (gray2, gray2, gray2)

        gray3 = math.floor(.21*r + .72 * g + .07*b)
        c_buffer[x+width, y + height] = (gray3, gray3, gray3)


container.save("hi.png", "png")



#image.save("out.png", "png")

# for i in range(8):
  #  image.save("out" + str(i) + ".png", "png") 

