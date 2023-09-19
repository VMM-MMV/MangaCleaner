import cv2
import easyocr
import main  # Import your main module

def perform_ocr_on_region(image, region_coords, reader):

    minx, miny, maxx, maxy = region_coords
    region = image[miny:maxy, minx:maxx]
    detected_text = ""
    try:
        results = reader.readtext(region)
        detected_text = ' '.join([result[1] for result in results])
    except:
        pass

    return detected_text, region_coords

def preprocess_image(image):
 
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    return gray_img

def ocr():
    reader = easyocr.Reader(['en'])

    image_path = 'img/003.jpg'
    img = cv2.imread(image_path)

    if img is None or img.size == 0:
        print("Error: Image is empty or not loaded correctly.")
    else:
        # Preprocess the image
        preprocessed_img = preprocess_image(img)

        # Call the clean_manga function from the main module to get region coordinates
        regions = main.clean_manga(image_path)

        # Iterate through regions, perform OCR, and add text and bounding boxes to the image
        for i, region_coords in enumerate(regions, start=1):
            detected_text, region_coords = perform_ocr_on_region(preprocessed_img, region_coords, reader)

            # Draw bounding box on the original image
            minx, miny, maxx, maxy = region_coords
            cv2.rectangle(img, (minx, miny), (maxx, maxy), (0, 255, 0), 2)  # Green bounding box
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, detected_text, (minx, miny - 10), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

            print(f"Region {i} Text: {detected_text}")

        # Save the image with bounding boxes and text
        output_image_path = 'img/output.jpg'
        cv2.imwrite(output_image_path, img)
        print(f"Output image with bounding boxes and text saved as {output_image_path}")

if __name__ == "__main__":
    ocr()
