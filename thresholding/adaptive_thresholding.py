# adaptive_thresholding.py


import cv2
import argparse
import numpy as np


'''
    In order to overcome this problem (The problem of manual decision of T),
    we can use adaptive thresholding, which considers small neighbors of pixels
    and then finds an optimal threshold value T for each neighbor.
    This method allows us to handle cases where there
    may be dramatic ranges of pixel intensities and the optimal value of T may
    change for different parts of the image.

        cv2.adaptiveThreshold(image, T_max, neigh_thresh_method, binary_tresh_method, neigh_size, C)

            + The first parameter we supply is the image we want to threshold.
            + Second parameter is Maximum Value of pixel (value it will be assigned)
            + The third argument is our method to compute the thresh- old for the
              current neighborhood of pixels.
            + The fourth parameter is the thresholding method
            + The fifth parameter is our neighborhood size. This integer value must
              be odd and indicates how large our neigh- borhood of pixels is going to be
            + Sixth parameter (called C). This value is an integer that is subtracted
              from the mean, allow- ing us to fine-tune our thresholding.

        By supplying cv2.ADAPTIVE_THRESH_MEAN_C, we indicate that we want to compute
        the mean of the neighborhood of pixels and treat it as our T value.

        We use cv2.ADAPTIVE_THRESH_GAUSSIAN_C to indicate we want to use the weighted mean.
    
    In general, choosing between mean adaptive threshold- ing and Gaussian adaptive
    thresholding requires a few ex- periments on your end. The most important
    parameters to vary are the neighborhood size and C, the value you subtract
    from the mean. By experimenting with this value, you will be able to dramatically
    change the results of your thresholding.

    
'''

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path tp image", default = 'images/coins.jpg')
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blurred, 120, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY_INV, 5, 6)
cv2.imshow("Mean Thresh", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY_INV, 5, 6)

cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)