from PIL import Image, ImageDraw, ImageFilter, ImageOps
import pytesseract

def draw_boxes_on_image(img, output_path):
    draw = ImageDraw.Draw(img)
    boxes = pytesseract.image_to_boxes(img)
    for box in boxes.splitlines():
        b = box.split()
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        draw.rectangle([x, img.height - h, w, img.height - y], outline="green")
    img.save(output_path)

def process_and_detect(img_path, output_prefix):
    original_img = Image.open(img_path)
    draw_boxes_on_image(original_img.copy(), f'{output_prefix}_original.png')

    # Convert to grayscale
    gray_img = original_img.convert('L')
    draw_boxes_on_image(gray_img, f'{output_prefix}_gray.png')

    # Binarization using Otsu's thresholding
    threshold = 128
    binarized_img = gray_img.point(lambda p: p < threshold and 255)
    draw_boxes_on_image(binarized_img, f'{output_prefix}_binarized.png')

    # Resize (enlarge)
    resized_img = original_img.resize((original_img.width*2, original_img.height*2), Image.BICUBIC)
    draw_boxes_on_image(resized_img, f'{output_prefix}_resized.png')

    # Denoise
    denoised_img = gray_img.filter(ImageFilter.MedianFilter(5))
    draw_boxes_on_image(denoised_img, f'{output_prefix}_denoised.png')

    # Enhanced Contrast
    enhanced_contrast_img = ImageOps.autocontrast(original_img)
    draw_boxes_on_image(enhanced_contrast_img, f'{output_prefix}_enhanced_contrast.png')

    print("Processing and detection complete. Please check the generated images.")

img_path = 'img.jpg'
process_and_detect(img_path, 'processed')
