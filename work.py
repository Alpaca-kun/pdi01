from PIL import Image
import numpy as np

original_image = np.array(Image.open("./images/cat.png"))

# An array to store the arrays a, b and c
n = np.empty(3, dtype=object)

print("Put three numbers to define the arrays size: ")

# Read the inputs and create a new colorbar for each input
for i in range(len(n)):
    array_size = int(input())
    n[i] = np.linspace(0, 255, num=array_size, dtype=int)

# Mesh all the colorbands and create a new RGB bar
modified_rgb_band = np.array(np.meshgrid(n[0], n[1], n[2])).T.reshape(-1, 3)

# print(original_image.shape)
# print(original_image[:,:,None].shape)
# print(modified_rgb_band[None, None, :])
# print(modified_rgb_band[None, None, :].shape)

# Calculate the distance between the colorbar of the original image with new 
# colorband. The slicing simplisly skip the xy coordenates and access directly
# the RGB values. So, the axis=3 set up the axis that contain the RGB arrays
distance = np.linalg.norm(original_image[:,:,None] -
                          modified_rgb_band[None,None,:], axis=3)

print(distance.shape)

# The axis=2 set up the coordinate of all color combinations
modified_image = np.argmin(distance, axis=2)
rgb_img = modified_rgb_band[modified_image]

# Convert the array to uint8 again and save it
pil_image = Image.fromarray(rgb_img.astype(np.uint8))
pil_image.save("./images/modified_cat.png")

# Image.fromarray(rgb_img).save("./images/modified_cat.png")
