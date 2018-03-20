# import packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from matplotlib import pyplot as plt

#Construct and Parse The Argument 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(parser.parse_args())

# Load an color image in grayscale 
img = cv2.imread(args["image"],0)

filename = "{}.png".format(os.getpid())
print(filename)
cv2.imwrite(filename, img)

# Load the image using PIL (Python Imaging Library), Apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(Image.open(filename))
print(text)
os.remove(filename)
 
# Display output images

#cv2.imshow("Image", img)
#cv2.waitKey(0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()