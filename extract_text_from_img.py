from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = r'C:\Users\Siddhi Doiphode\Pictures\image.png'

image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)

print(extracted_text)



