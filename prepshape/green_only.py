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

# Find the contours of the green regions
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming there's only one green region, select the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# Fit a Bézier curve to the contour points
x, y = largest_contour[:, 0, 0], largest_contour[:, 0, 1]
t = np.linspace(0, 1, len(x))
spl = make_interp_spline(t, np.c_[x, y], k=3)
curve = spl(np.linspace(0, 1, 100))

# Perform further analysis or computations on the curve
curve_length = cv2.arcLength(largest_contour, True)

# Print the length of the curve
print("Curve length:", curve_length)

# Visualize the curve
image_with_curve = image.copy()
cv2.polylines(image_with_curve, np.int32([curve]), isClosed=False, color=(0, 255, 0), thickness=2)

# Display the image with the curve
cv2.imshow('Image with Curve', image_with_curve)
cv2.waitKey(0)
cv2.destroyAllWindows()