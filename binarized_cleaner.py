import numpy as np

def lines(np_image, current, size):
    li = []
    for i in range(current, size):
        li.append(np_image[i])
    return li

def pacman(lines, size):
    li = []
    check = 0
    coords = []
    for i in range(len(lines)):
        small_coords = []
        first_column = 0
        second_column = 0
        for j in range(size):
            print(lines[j][i], lines[j][i+size-1], " ", check, i, j)
            # if sum(lines[0][:size]) == 0: 
            #     check += 1
            #     small_coords.append(lines[i][j])
            #     small_coords.append(lines[i][])
            # if sum(lines[len(lines)][:size]) == 0:
            #     check += 1
            # if check >= 2:
            #     first_column += lines[j][i]
            #     second_column += lines[j][i+size-1]


def clean_binarized_outliers(image):
    np_image = np.array(image)
    pacman(lines(np_image, 0, 100), 100)
    # for i in range(np_image.shape[0]):
    #     print(np_image[i])