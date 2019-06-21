from PIL import Image
import numpy as np
import math as mt

original_image = np.array(Image.open("./images/cat.png"))

number_of_cubes = 32

def median_cut_function (cube, n):
    if (n == 1):
        return cube
    else:
        diff_RGB = np.zeros(3)

        for i in range(len(diff_RGB)):

