from PIL import Image
import numpy as np

def median_cut_function(cube, n):
    if (n == 1):
        global old_color
        global replaced_color

        median_color = np.median(cube[:], axis=0)
        cube = np.unique(cube[:],axis=0)

        return old_color.append(cube), replaced_color.append(median_color)

    else:
        diff_RGB = np.zeros(3)

        for i in range(len(diff_RGB)):
            # For each color channel, calcule the diff between the max and min values
            diff_RGB[i] = cube[:,i].max() - cube[:,i].min()

        # Obtain the color channel index with greater distance
        greater_diff_channel = diff_RGB.argmax()

        # Slice the channel based in the median
        median_of_channel = np.floor(np.median(cube[:,greater_diff_channel]))
        left_side = cube[cube[:,greater_diff_channel] <= median_of_channel]
        right_side = cube[cube[:,greater_diff_channel] > median_of_channel]

        return median_cut_function(left_side, n/2), median_cut_function(right_side, n/2)

# ----- Main -----#
original_image = np.array(Image.open("./images/cat.png"))
image_dimensions = original_image.shape

number_of_cubes = 4

old_color = []
replaced_color = []

# Reshaping the original image dimensions to convert it in 2D-array
img_2D_array = np.reshape(original_image, (image_dimensions[0] * image_dimensions[1], 
                            image_dimensions[2]))
call_MCF = median_cut_function(img_2D_array, number_of_cubes)

print(replaced_color)
#pil_image = Image.fromarray(new_image.astype(np.uint8))
#pil_image.save("./images/b_cat.png")
