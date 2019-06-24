import numpy  
import math
from PIL import Image

original = numpy.array(Image.open("./images/cat.png"))
contrast = numpy.array(Image.open("./images/b_16.png"))

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )

    if mse == 0:
        return 100

    PIXEL_MAX = 255.0

    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d = psnr(original,contrast)
print(d)
