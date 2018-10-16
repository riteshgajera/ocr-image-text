from data import Data
from PIL import Image
import pytesseract
import cv2
import os


class TestData:

    @staticmethod
    def get():
        data = Data()
        data.set('Filename', 'in.jpg')
        data.set('Extracted text', 'abc xxx def')
        return data

    @staticmethod
    def extract(filename):
        UPLOADED_FILE = '/Users/abhijitpatil/temp/'+filename
        img = cv2.imread(UPLOADED_FILE)
        print("## img: " + UPLOADED_FILE)
        filename = "{}.png".format(os.getpid())
        print(filename)
        cv2.imwrite(filename, img)

        # Load the image using PIL (Python Imaging Library), Apply OCR, and then delete the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        print(text)
        os.remove(filename)
        return text