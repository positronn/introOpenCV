# masking.py

import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/alien.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# zeros mask
mask = np.zeros(image.shape[:2], dtype = "uint8")

# getting center of image
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

# drawing rectangle in mask
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

# getting image region where mask is located
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask applied to image", masked)


mask = np.zeros(image.shape[:2], dtype = 'uint8')
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask to image circle", mask)
cv2.imshow("Mask Applied to Image circle", masked)

cv2.waitKey(0)
