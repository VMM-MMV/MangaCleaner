from PIL import Image, ImageDraw
import numpy as np
from test import *

#  with open("output.txt", "w") as f:
#             # Convert numpy array row to string and write to file
#             f.write(' '.join(map(str, np_image[i])))

def clean_manga(img, name="sss"):
    original_img = Image.open(img)

    gray_img = original_img.convert('L')

    threshold = 254
    binarized_img = gray_img.point(lambda p: p < threshold and 255)

    boxes = get_scattered_text_line_coordinates_into_boxes(binarized_img)
    bboxes=get_text_box_that_encompases_text_line_coords(boxes)
    for bbox in bboxes:
        min_x, min_y, max_x, max_y = bbox
        SIZE=1

        original_img[min_x/SIZE: min_y/SIZE,max_x*SIZE: max_y*SIZE]=(0,0,0)
        
    
    # np_image = np.array(binarized_img)
    # # Go through each line of the image
    # for i in range(np_image.shape[0]):
    #     coordinates = get_start_and_end_coordinates_of_bundle(np_image[i])
    #     for cord in coordinates:
    #         draw.line([(cord[0], i), (cord[1], i)], fill="black", width=100)

    original_img.save(f"img/cleaned_{name}.jpg")
    binarized_img.save(f"img/binarized_{name}.jpg")
    return bboxes
if __name__ =="__init__":
    clean_manga("img/003.jpg")

