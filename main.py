from PIL import Image, ImageDraw, ImageFilter, ImageOps
import pytesseract
import cv2
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



# Your initial code:
original_img = Image.open('img.jpg')
draw = ImageDraw.Draw(original_img)
gray_img = original_img.convert('L')
threshold = 254
binarized_img = gray_img.point(lambda p: p < threshold and 255)

# Convert PIL image to OpenCV format
np_image = np.array(binarized_img)

# Get half width for transformation logic
half_width = np_image.shape[1] // 2

# Go through each line
for i in range(np_image.shape[0]):
    if i == 150:
        with open("output.txt", "w") as f:
            # Convert numpy array row to string and write to file
            f.write(' '.join(map(str, np_image[i])))
        
        index = detect_alternating_pattern(np_image[i])
        print(index)
        np_image[i] = 0  # Set the entire row to black
