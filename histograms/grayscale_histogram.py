# grayscale_histogram.py

from matplotlib import pyplot as plt


import cv2
import argparse

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/medusas.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", image)

hist = cv2.calcHist([image], [0],None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)