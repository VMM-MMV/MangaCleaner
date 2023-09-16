from PIL import Image, ImageDraw, ImageFilter, ImageOps
import pytesseract
import cv2
import numpy as np
from test import *

#  with open("output.txt", "w") as f:
#             # Convert numpy array row to string and write to file
#             f.write(' '.join(map(str, np_image[i])))

# Your initial code:
original_img = Image.open('img.jpg')
draw = ImageDraw.Draw(original_img)
gray_img = original_img.copy().convert('L')
threshold = 254
binarized_img = gray_img.point(lambda p: p < threshold and 255)

# Convert PIL image to OpenCV format
np_image = np.array(binarized_img)


# Go through each line
# for i in range(np_image.shape[0]):
#     try:
#         # print(np_image[i])
#         coordinates = return_start_and_end_coordinates_of_bundle(np_image[i])
#         if coordinates:
#             for cord in coordinates:
                
#                 draw.line([(cord[0], i), (cord[1], i)], fill="black", width=5)
#         print(coordinates)
#         with open("aa.txt", "a") as f:
#                 # Convert numpy array row to string and write to file
#             f.write(f'{coordinates}\n')
#     except:
#         pass

for i in range(np_image.shape[0]):
    if i == 4040:
        with open("output.txt", "w") as f:
            # Convert numpy array row to string and write to file
            f.write(' '.join(map(str, np_image[i])))
    
new_image = Image.fromarray(np_image)
new_image.save("b.jpg")
original_img.save("a.jpg")
