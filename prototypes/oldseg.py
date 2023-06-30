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

# Find the contours of the green regions
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Count the number of contours
num_contours = len(contours)

# Print the result
print("Number of contours: ", num_contours)

# Assuming there are two green regions bounding the DNA, select the two largest contours
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
if len(sorted_contours) < 2:
    print("Insufficient green regions found.")
    exit()

# Combine the two largest contours into a single contour
combined_contour = np.concatenate((sorted_contours[0], sorted_contours[1]))

# Fit a Bézier curve to the contour points
x, y = combined_contour[:, 0, 0], combined_contour[:, 0, 1]
t = np.linspace(0, 1, len(x))
spl = make_interp_spline(t, np.c_[x, y], k=3)
curve = spl(np.linspace(0, 1, 100))

# Draw the shape traversing through the dark area between the green regions
image_with_shape = image.copy()
cv2.polylines(image_with_shape, np.int32([curve]), isClosed=False, color=(0, 0, 255), thickness=2)

# Display the image with the shape
cv2.imshow('Image with Shape', image_with_shape)
cv2.waitKey(0)
cv2.destroyAllWindows()