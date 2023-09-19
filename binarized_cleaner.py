import numpy as np

def lines(np_image, current, size):
    li = []
    for i in range(current, size):
        li.append(np_image[i])
    return [li, current, size]

def pacman(lines):
    current = lines[1]
    size = lines[2]
    lines = lines[0]

    li = []
    check = 0
    coords = []
    for i in range(len(lines)):
        small_coords = []
        first_column = 0
        last_column = 0
        for j in range(size):
            if sum(lines[0][:size]) == 0: 
                check += 1
                small_coords.append((lines[j][i], current + j))
                small_coords.append((lines[j+size-1][i+size-1], current + j))
            if sum(lines[len(lines)][:size]) == 0:
                check += 1
            if check >= 2:
                first_column += lines[j][i]
                last_column += lines[j][i+size-1]
        if first_column == 0:
            check += 1
        if last_column == 0:
            check += 1
        if check == 4:
            coords.append(small_coords)
    print(coords)


def clean_binarized_outliers(image):
    np_image = np.array(image)
    for i in range(np_image.shape[0]):
        pacman(lines(np_image, i, 100))