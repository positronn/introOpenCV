# arithmetic.py

import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/alien.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# opencv arithmetic
print("max of 255 (+): {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0   (-): {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# numpy arithmetic
# In additionm once a value of 255 is reached, NumPy wraps around to zero,
# and then starts counting up again, until 100 steps have been reached.
# Instead, once 0 is reached during the subtraction, the modulos operations
# wraps around and starts counting backwards from 255
print("wrap around (+): {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around (-): {}".format(np.uint8([200]) - np.uint8([100])))


M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)