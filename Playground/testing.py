from PIL import Image
import numpy

zero = Image.open("zero.png")
pix = numpy.array(zero)
total = 0
image = []
for x in numpy.nditer(pix):
    if total%3==0:
        image.append(1-x/255)
    total += 1
for item in image:
    print(item,end=',')

#print(total, end=' ')