import cv2
import numpy as np
from scipy.interpolate import splprep, splev
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

# Assuming there are multiple green regions bounding the DNA, select the largest contours
num_contours = 10  # Set the desired number of contours
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:num_contours]

# Create an empty image to draw the contours
contour_image = np.zeros_like(image)

# Draw the contours on the image
cv2.drawContours(contour_image, sorted_contours, -1, (0, 255, 0), 2)

# Extract contour points from the largest contours
contour_points = []
for contour in sorted_contours:
    for point in contour:
        contour_points.append(point[0])

# Convert the contour points to numpy array
contour_points = np.array(contour_points)

# Extract x and y coordinates from the contour points
x, y = contour_points[:, 0], contour_points[:, 1]

# Fit a NURBS curve to the contour points
tck, u = splprep([x, y], s=0, per=1)

# Generate points on the NURBS curve
u_new = np.linspace(u.min(), u.max(), 100)
x_new, y_new = splev(u_new, tck)

# Draw the NURBS curve on the contour image
nurbs_image = contour_image.copy()
curve_pts = np.column_stack((x_new, y_new)).astype(np.int32)
cv2.polylines(nurbs_image, [curve_pts], isClosed=False, color=(0, 0, 255), thickness=2)

# Display the original image, contour image, and NURBS image
cv2.imshow('Original Image', image)
cv2.imshow('Contour Image', contour_image)
cv2.imshow('NURBS Image', nurbs_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
