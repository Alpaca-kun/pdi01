from PIL import Image
import numpy as np

original_image = np.array(Image.open("./images/cat.png"))

# An array to store the arrays a, b and c
n = np.empty(3, dtype=object)

print("Put three numbers to define the arrays size: ")

for i in range(len(n)):
    array_size = int(input())
    n[i] = np.linspace(0, 255, num=array_size, dtype=int)
    
    print(n[i])

