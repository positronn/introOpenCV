# sobel_and_laplacian.py

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
cv2.imshow("Image", image)


'''
    Transitioning from black-to-white is considered a positive slope, whereas a
    transition from white-to-black is a negative slope. 

    An 8-bit unsigned integer does not represent negative values. Either it will
    be clipped to zero if you are using OpenCV or a modulus operation will be
    performed using NumPy.

    The short answer here is that if you don’t use a floating point data type
    when computing the gradient magnitude image, you will miss edges,
    specifically the white-to-black transitions.
'''
# Laplacian
lap = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("Laplacian 0", lap)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian 1", lap)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Sobel
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelX_1 = sobelX.copy()
sobelCombined = cv2.bitwise_or(sobelY, sobelX_1)

cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Combined", sobelCombined)

print(sobelX == sobelCombined)
cv2.waitKey(0)

cv2.destroyAllWindows()