# crop.py

import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'alien.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[30:220, 30:335]
cv2.imshow("Alien Face", cropped)
cv2.waitKey(0)
