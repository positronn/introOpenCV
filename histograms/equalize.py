# equalize.py

import cv2
import argparse
import numpy as np

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/medusas.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)