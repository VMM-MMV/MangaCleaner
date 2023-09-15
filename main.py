from PIL import Image, ImageDraw, ImageFilter, ImageOps
import pytesseract
import cv2
import numpy as np

def has_concentrated_edges(box, edges):
    x, y, w, h = box
    roi = edges[y:y+h, x:x+w]
    
    total_pixels = roi.size
    edge_pixels = np.sum(roi)/255.0
    
    concentration = edge_pixels / total_pixels

    return concentration > 0.10

def draw_boxes_on_image(img, output_path, boxes):
    draw = ImageDraw.Draw(img)
    custom_config = r'--oem 3 --psm 11'
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, config=custom_config)
    
    np_img = np.array(img)
    
    # Use Canny Edge Detection on the numpy array
    edges = cv2.Canny(np_img, 100, 200)

    for i in range(len(data['level'])):
        if data['level'][i] == 4:  # Word level
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            if has_concentrated_edges((x, y, w, h), edges) and (w * h) > 2000:
                draw.rectangle([x-5, y-5, x + w + 5, y + h + 5], fill="black", width=1000)
                boxes.append([x-5, y-5, x + w + 5, y + h + 5])

    img.save(output_path)
    return boxes

def process_and_detect(img_path, output_prefix):
    original_img = Image.open(img_path)

    # Convert to grayscale
    gray_img = original_img.convert('L')
    # draw_boxes_on_image(gray_img, f'{output_prefix}_gray.png', [])

    draw = ImageDraw.Draw(original_img)
    # Binarization using Otsu's thresholding
    threshold = 254
    binarized_img = gray_img.point(lambda p: p < threshold and 255)
    for i in draw_boxes_on_image(binarized_img, f'{output_prefix}_binarized.png', []):
        draw.rectangle(i, fill="white", width=1000)
    original_img.save('a.png')

img_path = 'img.jpg'
process_and_detect(img_path, 'processed')

