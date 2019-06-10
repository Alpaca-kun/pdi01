from PIL import Image
import numpy as np

im = np.array(Image.open("../images/cat.png"))

# Testing print functions 
print(im.dtype) # print the Data Type of image (uint8)
print(im.ndim) # print the Number of Dimension of image
print(im.shape) # print the Shape of image (Height * Weight * Colors)


