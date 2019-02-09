# counting_coins.py

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
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)


'''
    The first argument to cv2.findContours is our edged im- age. It’s important
    to note that this function is destructive to the image you pass in.
    If you intend using that image later on in your code, it’s best to make a copy of it.

    The second argument is the type of contours we want.
    We use cv2.RETR_EXTERNAL to retrieve only the outermost contours (i.e., the
    contours that follow the outline of the coin). We can also pass in cv2.RETR_LIST
    to grab all con- tours. Other methods include hierarchical contours
    using cv2.RETR_COMP and cv2.RETR_TREE.

    
    Our last argument is how we want to approximate the contour.
    We use cv2.CHAIN_APPROX_SIMPLE to compress horizontal, vertical, and diagonal
    segments into their end- points only. This saves both computation and memory.
    If we wanted all the points along the contour, without com- pression, we can pass
    in cv2.CHAIN_APPROX_NONE; however, be very sparing when using this function.
    Retrieving all points along a contour is often unnecessary and is wasteful of resources.

    This method returns a 3-tuple of: (1) our image after applying contour
    detection (which is modified and essentially destroyed), (2) the contours
    themselves, cnts, and (3) the hierarchy of the contours.
'''
(__, cnts, hierarchy) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image".format(len(cnts)))
print("hierarchy: {}".format(hierarchy))


coins = image.copy()
'''
    A call to cv2.drawContours draws the actual contours on our image.
    The first argument to the function is the image we want to draw on.
    The second is our list of contours. Next, we have the contour index.
    By specifying a negative value of −1, we are indicating that we want to
    draw all of the contours. However, we would also supply an index i,
    which would be the i’th contour in cnts. This would allow us to draw only
    a single contour rather than all of them.

    The fourth argument to the cv2.drawContours function is the color of the
    line we are going to draw. Here, we use a green color.


    Finally, our last argument is the thickness of the line we are drawing. We’ll
    draw the contour with a thickness of two pixels.
'''
for i in range(0, 12):
    cv2.drawContours(coins, cnts, i , (0, 255, 0), 2)

cv2.imshow("Coins", coins)
cv2.waitKey(0)


cv2.destroyAllWindows()