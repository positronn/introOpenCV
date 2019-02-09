# rotation.py

import cv2
import imutils
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'alien.jpg')
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees", rotated)


M = np.float32([[ 0.70710678, 0.70710678, 0], [-0.70710678, 0.70710678, 0]])
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted down and right", shifted)



M = imutils.getMyRotationMatrix(image = image, center = None, theta = 45, scale = 1.0)
shifted = cv2.warpAffine(image, M, (w, h))
cv2.imshow("MyImplementation", shifted)


rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()