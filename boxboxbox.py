from PIL import Image, ImageDraw
import numpy as np
import main
import cv2 



img="img/003.jpg"
bboxes=main.clean_manga(img)
original_img = Image.open(img)
gray_img = original_img.convert('L')

threshold = 254
binarized_img = np.array(gray_img.point(lambda p: p < threshold and 255))

binarized_img_cpy=binarized_img.copy()
original_img = np.array(Image.open(img))


print(binarized_img.shape)

N=64
SIZE=int(binarized_img.shape[1]/N)

boundsX=np.arange(binarized_img.shape[1]+1)[0:binarized_img.shape[1]+1][::SIZE]
boundsY=np.arange(binarized_img.shape[0]+1)[0:binarized_img.shape[0]+1][::SIZE]

print( boundsX,boundsY)

def overlapSquares(squares,test_coords):    
    overlap = any(
        test_coords[0] >= square[0] and
        test_coords[2] <= square[2] and
        test_coords[1] >= square[1] and
        test_coords[3] <= square[3]
        for square in squares
    )

    return overlap
def check_color_and_fill(square, image):
    # Extract the coordinates of the square
    x1, y1, x2, y2 = square

    # Extract the outer border of the square
    outer_square = image[y1:y2, x1:x2]

    # Extract the inner part of the square
    inner_square = image[y1+1:y2-1, x1+1:x2-1]

    # Check if all the border pixels have the same color
    if np.all(outer_square == outer_square[0, 0]):
        # Check if there's a different color inside the square
        if not np.all(inner_square == inner_square[0, 0]):
            # Fill the square with white color
            image[y1:y2, x1:x2] = (255, 255, 255)

    return image
for i in range(len(boundsX) - 1):
    for j in range(len(boundsY) - 1):
        square = [boundsX[i], boundsY[j], boundsX[i + 1], boundsY[j + 1]]
        notText=overlapSquares(bboxes, square)
        if not notText:
            
            result_img = check_color_and_fill(square, binarized_img)

cv2.imwrite("img/rect.jpg", result_img)


