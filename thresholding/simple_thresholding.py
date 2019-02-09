# simple_thresholding.py

'''
    Thresholding is the binarization of an image. In general, we seek to
    convert a grayscale image to a binary image, where the pixels are either 0 or 255.

    Normally, we use thresholding to focus on objects or ar- eas of particular
    interest in an image. In the examples in the sections below, we will empty our
    pockets and look at our spare change. Using thresholding methods, we’ll be able
    to find the coins in an image.
'''


'''
    Applying simple thresholding methods requires human in- tervention. We must
    specify a threshold value T. All pixel intensities below T are set to 0. And
    all pixel intensities greater than T are set to 255.

    We can also apply the inverse of this binarization by setting all pixels
    below T to 255 and all pixel intensities greater than T to 0.
'''

import cv2
import argparse
import numpy as np


# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/coins.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3)
# cv2.imshow("Original", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
# cv2.imshow("Image", image)

(T, thresh) = cv2.threshold(blurred, 145, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 145, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

cv2.imshow("Coins INV B_AND", cv2.bitwise_and(image, image, mask = threshInv))
cv2.imshow("Coins B_AND", cv2.bitwise_and(image, image, mask = thresh))


cv2.waitKey(0)