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

# Assuming there are two green regions bounding the DNA, select the two largest contours
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
if len(sorted_contours) < 2:
    print("Insufficient green regions found.")
    exit()

# Combine the two largest contours into a single contour
combined_contour = np.concatenate((sorted_contours[0], sorted_contours[1]))

# Smooth the combined contour using the Douglas-Peucker algorithm
epsilon = 0.01 * cv2.arcLength(combined_contour, True)
smoothed_contour = cv2.approxPolyDP(combined_contour, epsilon, True)

# Visualize the smoothed contour on the image
image_with_contour = image.copy()
cv2.drawContours(image_with_contour, [smoothed_contour], -1, (0, 255, 0), 2)

# Display the image with the contour
cv2.imshow('Image with Contour', image_with_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()