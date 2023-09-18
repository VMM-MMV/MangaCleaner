from PIL import Image, ImageDraw
import numpy as np
from test import *
from binarized_cleaner import *

#  with open("output.txt", "w") as f:
#             # Convert numpy array row to string and write to file
#             f.write(' '.join(map(str, np_image[i])))

def clean_manga(img, name):
    original_img = Image.open(img)
    draw = ImageDraw.Draw(original_img)

    gray_img = original_img.convert('L')

    threshold = 254
    binarized_img = gray_img.point(lambda p: p < threshold and 255)

    clean_binarized_outliers(binarized_img)
    # boxes = get_scattered_text_line_coordinates_into_boxes(binarized_img)

    # # for i in boxes:
    # #     print(i)

    # # for box in boxes:
    # #     for i in box:
    # #         draw.line([(i[1], i[0]), (i[2], i[0])], fill="red", width=5)
    # for bbox in get_text_box_that_encompases_text_line_coords(boxes):
    #     min_x, min_y, max_x, max_y = bbox
    #     draw.rectangle([min_x, min_y, max_x, max_y], fill="black")

    original_img.save(f"cleaned_{name}.jpg")

for i in range(1,2):
    clean_manga(r'/home/miguel/Downloads/image/1000{}.jpg'.format(i), i)