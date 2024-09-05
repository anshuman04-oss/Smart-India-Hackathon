import cv2
from PIL import Image
import pytesseract

img_path = "C:\\Users\\ANSHUMAN\\OneDrive\\Pictures\\profile.jpg"

im = Image.open(img_path)

print(im.size)
im.show()