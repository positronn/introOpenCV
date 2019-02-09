# imutils.py

import cv2
import numpy as np



def translate(image:np.ndarray, t_x:float, t_y:float) -> np.ndarray:
    '''
        Applies a translation transformation to an image according to
        the Matrix:

                    [1, 0, t_x]
            M =     [0, 1, t_y]
                    [0, 0,  1 ]

        ** opencv doesn't expect the last row because it is trivial for
        image geometric transformations: image representation is sufficient
        within 2 dimensions.

        parameters
        ----------
            image: image to be transformed
            t_x: pixels to be translated in x axis (if t_x > 0 moves to right, else to left)
            t_y: pixels to be translated in y axis (if t_y > 0 moves down, else up)

        returns
        -------
            shifted: image with applied translation transformation
    '''
    M = np.float32([
                    [1, 0, t_x],
                    [0, 1, t_y]
        ])

    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return shifted



def getMyRotationMatrix(image:np.ndarray, theta:float, scale = 1.0,  center = None) -> np.ndarray:
    '''
    '''

    if center is None:
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)

    print("theta grad: ", theta)
    theta = np.radians(theta)
    print("theta rad: ", theta)
    alpha = scale * np.cos(theta)
    beta = scale * np.sin(theta)

    M = np.float32([
            [alpha, beta, (1 - alpha) * center[0] - beta * center[1]],
            [-beta, alpha, beta * center[0] + (1 - alpha) * center[1]]
    ])

    return M



def rotate(image, angle, center = None, scale = 1.0):
    '''
    '''

    (h, w) = image.shape[:2]

    if center is None:
        center = (w // 2, h // 2)


    print(angle)
    M = getMyRotationMatrix(image, angle, scale, center = center)
    print("My matrix: \n", M)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    print("Opencv matrix: \n", M)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated



def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    '''
    '''
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), heiht)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized
