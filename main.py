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

# Convert PIL image to OpenCV format
np_image = np.array(binarized_img)

# Get half width for transformation logic
half_width = np_image.shape[1] // 2

# Go through each line
for i in range(np_image.shape[0]):
    try:
        # print(np_image[i])
        coordinates = return_start_and_end_coordinates_of_bundle(np_image[i])
        if coordinates:
            for cord in coordinates:
                draw.line([(cord[0], i), (cord[1], i)], fill="black", width=115)

original_img.save("a.jpg")
