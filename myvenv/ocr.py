import pytesseract as pt
from PIL import Image
import cv2

class ocr:
    def __init__(self,image):
        self.im = image

    def predicting(self):
         print(pt.image_to_string(Image.open(self.im)))


# x = ocr("B.png")
pt.image_to_string(Image.open("B.png"))
# z = Image.open("B.png")


    