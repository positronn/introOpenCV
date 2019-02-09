# canny.py

import cv2
import argparse
import numpy as np


# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/coins.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)


'''
    The first argument we supply (to Canny()) is our blurred, grayscale image.
    Then, we need to provide two values: threshold1 and threshold2

    Any gradient value larger than threshold2 is considered to be an edge.
    Any value below threshold1 is consid- ered not to be an edge. Values in
    between threshold1 and threshold2 are either classified as edges or non-edges
    based on how their intensities are “connected”. In this case, any gradient
    values below 30 are considered non-edges wh- ereas any values above 150 are
    considered edges.

    
'''
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)


cv2.destroyAllWindows()