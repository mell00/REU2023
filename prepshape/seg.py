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

# Visualize the DNA curve on the image
image_with_curve = image.copy()
cv2.polylines(image_with_curve, np.int32([curve]), isClosed=False, color=(0, 255, 0), thickness=2)

# Display the image with the DNA curve
cv2.imshow('Image with DNA Curve', image_with_curve)
cv2.waitKey(0)
cv2.destroyAllWindows()