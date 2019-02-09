# histogram_with_mask.py

import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt



def plt_histogram(image, title, mask = None):
    '''
    '''
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])

    plt.show()



# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/color.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
plt_histogram(image, "Histogram for Original Image")

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)


plt_histogram(masked, "Histogram for Original Image")

cv2.waitKey(0)
cv2.destroyAllWindows()