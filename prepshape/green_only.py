import cv2
import numpy as np
from scipy.interpolate import make_interp_spline
from prepshape import *

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the green color range
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Threshold the HSV image to get only the green regions
mask = cv2.inRange(hsv, lower_green, upper_green)

# Invert the mask to get non-green regions
non_green_mask = cv2.bitwise_not(mask)

# Create a white image
result = np.ones_like(image) * 255

# Copy green regions from the original image to the result
result[np.where(mask == 255)] = image[np.where(mask == 255)]


# Display the result
cv2.imshow('Green Regions with White Background', result)
cv2.waitKey(0)
cv2.destroyAllWindows()