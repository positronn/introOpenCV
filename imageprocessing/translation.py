# translation.py

import cv2
import imutils
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'alien.jpg')
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# definining traslation matrix (for geometric transformation)
'''
    M = [
        [1, 0, t_x],
        [0, 1, t_y],
        [0, 0, 1]
    ]

    opencv doesnt expect the last row because it is "trivial" for 2d images:
    there is no transformation in the z axis because we dont use it...
'''
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted down", shifted)


cv2.waitKey(0)
cv2.destroyAllWindows()
