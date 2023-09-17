import numpy as np
from PIL import Image, ImageDraw


def detect_alternating_pattern(arr):
    change_indices = np.where(np.diff(arr) != 0)[0] + 1

    change_indices = np.insert(change_indices, 0, 0)
    change_indices = np.append(change_indices, len(arr))

    segments = []
    for i in range(len(change_indices) - 1):
        start, end = change_indices[i], change_indices[i+1]
        segments.append((arr[start], end - start, start))

    return segments


def get_bundles_of_text(segments):
    bundles = []
    bundle = []

    for item in segments:
        if item[1] > 20:
            if len(bundle) > 7:
                bundles.append(bundle)
            bundle = []
        else:
            if item[1] > 5:
                bundle.append(item)

    # if len(bundle) > 7:
    #     bundles.append(bundle)
    # print(bundles)
    return bundles

def get_start_and_end_coordinates_of_bundle(line):
    coordinates = []
    segments = detect_alternating_pattern(line)
    bundles = get_bundles_of_text(segments)

    for bundle in bundles:
        coordinates.append((bundle[0][2], bundle[-1][2]))
    return coordinates


def get_scattered_text_line_coordinates_into_boxes(image):
    li = []
    small_li = []
    amount_of_null_lists = 0

    np_image = np.array(image)
    # Go through each line of the image
    for i in range(np_image.shape[0]):
            coordinates = get_start_and_end_coordinates_of_bundle(np_image[i])

            if coordinates:
                    amount_of_null_lists = 0
                    for coord in coordinates:
                        small_li.append((i, coord[0], coord[1])) 
            elif amount_of_null_lists > 30:
                    if small_li:
                        li.append(small_li)
                    small_li = []

            amount_of_null_lists += 1
    return li

def get_text_box_that_encompases_text_line_coords(many_text_line_coordinates_in_boxes):
    boxes = []

    for many_text_line_coordinates_in_box in many_text_line_coordinates_in_boxes:
        min_y = float('inf')
        max_y = float('-inf')
        min_x = float('inf')
        max_x = float('-inf')
        for text_line_coordinates in many_text_line_coordinates_in_box:
            y, x_start, x_end = text_line_coordinates
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            min_x = min(min_x, x_start)
            max_x = max(max_x, x_end)

        
        boxes.append((min_x-10, min_y-10, max_x+10, max_y+10))
    return boxes


if __name__ == "__main__":
    line = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,255,255,255,255,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,255,255,255,255,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])# Your array goes here

    coordinates = get_start_and_end_coordinates_of_bundle(line)

    image = Image.open('img.jpg')
    draw = ImageDraw.Draw(image)

    for cord in coordinates:
        draw.line([(cord[0], 150), (cord[1], 150)], fill="black", width=100)

    image.save("aa.jpg")