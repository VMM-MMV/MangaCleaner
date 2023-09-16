from PIL import Image, ImageDraw
import numpy as np

import numpy as np

def detect_alternating_pattern(arr, min_length=5):
    """
    Detects an alternating pattern of 255 and 0 in the array.
    :param arr: Input numpy array.
    :param min_length: Minimum length of alternating pattern to be detected.
    :return: Index where the pattern begins or None if not found.
    """
    
    n = len(arr)
    
    for i in range(n - min_length + 1):
        window = arr[i:i+min_length]
        differences = np.diff(window)  # Computes difference between consecutive elements
        if np.all(differences):  # If all differences are non-zero, it's an alternating pattern
            return i
    return None



original_img = Image.open('img.jpg')
draw = ImageDraw.Draw(original_img)
gray_img = original_img.copy().convert('L')
threshold = 254
binarized_img = gray_img.point(lambda p: p < threshold and 255)


def get_text_box(data):
    boxes = []

    for items in data:
        min_y = float('inf')
        max_y = float('-inf')
        min_x = float('inf')
        max_x = float('-inf')
        for item in items:
            y, x_start, x_end = item
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            min_x = min(min_x, x_start)
            max_x = max(max_x, x_end)

        
        boxes.append((min_x-10, min_y-10, max_x+30, max_y+20))
    return boxes


def get_scattered_text_in_boxes(image):
    li = []
    small_li = []
    amount_of_null_lists = 0

    np_image = np.array(image)
    # Go through each line
    for i in range(np_image.shape[0]):
            coordinates = return_start_and_end_coordinates_of_bundle(np_image[i])
            # if coordinates:
            #     for start, end in coordinates:
            #         draw.line([(start, i), (end, i)], fill="black", width=115)
            if coordinates:
                    amount_of_null_lists = 0
                    for coord in coordinates:
                        small_li.append((i, coord[0], coord[1])) 
            elif amount_of_null_lists > 25:
                    if small_li:
                        li.append(small_li)
                    small_li = []

            amount_of_null_lists += 1
    return li


li = get_scattered_text_in_boxes(binarized_img)

for bbox in get_text_box(li):
    min_x, min_y, max_x, max_y = bbox
    draw.rectangle([min_x, min_y, max_x, max_y], fill="white")

original_img.save("a_with_boxes.jpg")
