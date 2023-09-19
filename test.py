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
            if len(bundle) > 5:
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
            elif amount_of_null_lists > 200:
                    if small_li:
                        li.append(small_li)
                    small_li = []

            amount_of_null_lists += 1
    return li

def get_average(li):
    return int(sum(li) / len(li))
    
def get_median_lower(li):
    return sorted(li)[int(len(li)/4)]

def get_median_upper(li):
    return sorted(li)[int(len(li)/(1+(1/3)))]

def clean_page(image):
    np_image = np.array(image)
    # Go through each line of the image
    # for i in range(np_image.shape[0]):
    #     print(np_image[i])


def get_text_box_that_encompases_text_line_coords(many_text_line_coordinates_in_boxes):
    boxes = []

    for many_text_line_coordinates_in_box in many_text_line_coordinates_in_boxes:
        min_y = []
        max_y = []
        min_x = []
        max_x = []
        all_y = []
        for text_line_coordinates in many_text_line_coordinates_in_box:
            # print(text_line_coordinates)
            y, x_start, x_end = text_line_coordinates
            all_y.append(y)
            min_x.append(x_start)
            max_x.append(x_end)
        
        min_x = get_median_lower(min_x)
        max_x = get_median_upper(max_x)
        if len(all_y) >= 2: 
            min_y = sorted(all_y)
            min_y = min_y[:int(len(all_y)/2)]
            min_y = get_median_lower(min_y)

            max_y = sorted(all_y)
            max_y = max_y[int(len(all_y)/2):]
            max_y = get_median_upper(max_y)
        else:
            min_y = all_y[0]
            max_y = all_y[0]

        # if min_y and max_y and min_x and max_x:
        boxes.append((min_x-100, min_y-100, max_x+100, max_y+100))
    return boxes


