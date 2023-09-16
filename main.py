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

gray_img = original_img.convert('L')

threshold = 254
binarized_img = gray_img.point(lambda p: p < threshold and 255)

boxes = get_scattered_text_line_coordinates_into_boxes(binarized_img)

for bbox in get_text_box_that_encompases_text_line_coords(boxes):
    min_x, min_y, max_x, max_y = bbox
    draw.rectangle([min_x, min_y, max_x, max_y], fill="white")

for i in range(1,11):
    clean_manga(r'/home/miguel/Downloads/image/1000{}.jpg'.format(i), i)
