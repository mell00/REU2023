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

# Apply bitwise AND operation to isolate green regions
green_only = cv2.bitwise_and(image, image, mask=mask)

# Display the green regions only
cv2.imshow('Green Regions Only', green_only)
cv2.waitKey(0)
cv2.destroyAllWindows()
