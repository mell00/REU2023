'''import cv2
import numpy as np
from data import *

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform thresholding to obtain a binary image
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over each contour
for contour in contours:
    # Compute the convex hull of the contour
    hull = cv2.convexHull(contour)

    # Approximate the contour with fewer points
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Fit a circle to the approximate contour
    (x, y), radius = cv2.minEnclosingCircle(approx)
    center = (int(x), int(y))
    radius = int(radius)

    # Check if the radius is zero
    if radius > 0:
        # Calculate curvature as the inverse of the radius
        curvature = 1 / radius

        # Draw the contour, convex hull, and circle on the image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.drawContours(image, [hull], -1, (0, 0, 255), 2)
        cv2.circle(image, center, radius, (255, 0, 0), 2)


# Display the image
cv2.imshow('Curvature Analysis', image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import cv2
import numpy as np
from data import *

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform thresholding to obtain a binary image
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Set minimum contour area and aspect ratio thresholds
min_contour_area = 17
min_aspect_ratio = 0.2

# Iterate over each contour
for contour in contours:
    # Calculate contour area
    contour_area = cv2.contourArea(contour)

    # Skip contours with small area
    if contour_area < min_contour_area:
        continue

    # Calculate bounding rectangle for the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate aspect ratio of the bounding rectangle
    aspect_ratio = float(w) / h

    # Skip contours with low aspect ratio
    if aspect_ratio < min_aspect_ratio:
        continue

    # Approximate the contour with fewer points
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Fit a circle to the approximate contour
    (cx, cy), radius = cv2.minEnclosingCircle(approx)
    center = (int(cx), int(cy))
    radius = int(radius)

    # Check if the radius is zero
    if radius > 0:
        # Calculate curvature as the inverse of the radius
        curvature = 1 / radius

        # Draw the contour, bounding rectangle, and circle on the image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.circle(image, center, radius, (255, 0, 0), 2)

# Display the image
cv2.imshow('DNA Segmentation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
