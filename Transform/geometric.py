import math

import numpy as np

from .interpolation import interpolation


class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by and angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""

        row = len(image)
        col = len(image)
        new_row, new_col = 0, 0

        min_x, max_x = 0, 0
        min_y, max_y = 0, 0

        for i in range(0, row):
            for j in range(0, col):
                x = i * math.cos(theta) - j * math.sin(theta)
                y = i * math.sin(theta) + j * math.cos(theta)
                if max_x < x:
                    max_x = x
                if min_x > x:
                    min_x = x
                if max_y < y:
                    max_y = y
                if min_y > y:
                    min_y = y

        new_row, new_col = int(round(max_x - min_x)) + 1, int(round(max_y - min_y)) + 1

        rotated_image = np.zeros((new_row, new_col))

        for i in range(0, row):
            for j in range(0, col):
                x = (i * math.cos(theta)) - (j * math.sin(theta))
                y = (i * math.sin(theta)) + (j * math.cos(theta))
                x, y = int(round(x - min_x)), int(round(y - min_y))
                rotated_image[x][y] = image[i][j]

        return rotated_image

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by and angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""

        original_image = np.zeros(original_shape)
        row = len(rotated_image)
        col = len(rotated_image[0])
        original_row = len(original_image)
        original_col = len(original_image[0])

        for i in range(0, row):
            for j in range(0, col):
                xr = i - origin[0]
                yr = j - origin[1]
                x = int(round((xr * math.cos(theta)) + (yr * math.sin(theta))))
                y = int(round((yr * math.cos(theta)) - (xr * math.sin(theta))))
                if (0 <= x < original_row) and (0 <= y < original_col):
                    original_image[x][y] = rotated_image[i][j]

        return original_image

    def rotate(self, image, theta, interpolation_type):
        """Computes the reverse rotated image by and angle theta
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the original image"""
        row = len(image)
        col = len(image)
        new_row, new_col = 0, 0

        min_x, max_x = 0, 0
        min_y, max_y = 0, 0

        for i in range(0, row):
            for j in range(0, col):
                x = i * math.cos(theta) - j * math.sin(theta)
                y = i * math.sin(theta) + j * math.cos(theta)
                if max_x < x:
                    max_x = x
                if min_x > x:
                    min_x = x
                if max_y < y:
                    max_y = y
                if min_y > y:
                    min_y = y

        new_row, new_col = int(round(max_x - min_x) + 1), int(round(max_y - min_y) + 1)

        rotated_image = np.zeros((new_row, new_col))
        rotated_row = len(rotated_image)
        rotated_col = len(rotated_image[0])

        for i in range(0, row):
            for j in range(0, col):
                x = (i * math.cos(theta)) - (j * math.sin(theta))
                y = (i * math.sin(theta)) + (j * math.cos(theta))
                x, y = int(round(x - min_x)), int(round(y - min_y))
                rotated_image[x][y] = image[i][j]

        origin = [-min_x, -min_y]
        interpolation_transform = interpolation()

        if interpolation_type == "nearest_neighbor":
            for i in range(0, rotated_row):
                for j in range(0, rotated_col):
                    xr = i - origin[0]
                    yr = j - origin[1]
                    x = int(round((xr * math.cos(theta)) + (yr * math.sin(theta))))
                    y = int(round((yr * math.cos(theta)) - (xr * math.sin(theta))))
                    if (0 <= x < row) and (0 <= y < col):
                        rotated_image[i][j] = image[x][y]

        elif interpolation_type == "bilinear":
            for i in range(0, rotated_row):
                for j in range(0, rotated_col):
                    xr = i - origin[0]
                    yr = j - origin[1]
                    x = (xr * math.cos(theta)) + (yr * math.sin(theta))
                    y = (yr * math.cos(theta)) - (xr * math.sin(theta))
                    x0 = int(round(x))
                    y0 = int(round(y))
                    x1 = math.ceil(x - 1)
                    x2 = math.floor(x + 1)
                    y1 = math.ceil(y - 1)
                    y2 = math.floor(y + 1)
                    if (0 <= x0 < row) and (0 <= y0 < col):
                        if x1 < 0:
                            x1 = 0
                        if x1 >= row:
                            x1 = row-1
                        if x2 < 0:
                            x2 = 0
                        if x2 >= row:
                            x2 = row-1
                        if y1 < 0:
                            y1 = 0
                        if y1 >= col:
                            y1 = col-1
                        if y2 < 0:
                            y2 = 0
                        if y2 >= col:
                            y2 = col-1
                        rotated_image[i][j] = interpolation_transform.bilinear_interpolation([x1,y1,image[x1][y1]], [x1,y2,image[x1][y2]], [x2,y1,image[x2][y1]], [x2,y2,image[x2][y2]], [x,y,image[x0][y0]])

        return rotated_image
