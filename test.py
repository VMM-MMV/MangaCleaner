import numpy as np


def detect_alternating_pattern(arr):
    change_indices = np.where(np.diff(arr) != 0)[0] + 1

    change_indices = np.insert(change_indices, 0, 0)
    change_indices = np.append(change_indices, len(arr))

    segments = []
    for i in range(len(change_indices) - 1):
        start, end = change_indices[i], change_indices[i+1]
        segments.append((arr[start], end - start, start))

    return segments


def return_bundle_of_text(segments):
    li = []
    i = 0
    while(i < len(segments)-1):
        small_li = []
        
        while (segments[i][0] == 255) and (segments[i][1] >= 5) or ((segments[i][0] == 0) and (segments[i][0] <= 15)):
            small_li.append(segments[i])
            i += 1
        i += 1

        if(len(small_li) > 1):
            li.append(small_li)

    return sorted(li, key=len)[::-1]

def return_start_and_end_coordinates_of_bundle(bundles):
    for i in bundles:
        print(i[0][2], i[-1][2])

line = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,255,255,255,255,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,255,255,255,255,255,255,0,0,0,0,0,0,255,255,255,255,255,255,255,255,255,255,255,255,0,0,0,255,255,255,255,255,255,255,255,255,255,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,0,255,255,255,255,0,255,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])# Your array goes here
segments = detect_alternating_pattern(line)
bundles = return_bundle_of_text(segments)
return_start_and_end_coordinates_of_bundle(bundles)
