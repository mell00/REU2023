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
min_contour_area = 15
min_aspect_ratio = 0.25
# Calculate the distance between contours using the centroid of each contour
def calculate_distance(cnt1, cnt2):
    M1 = cv2.moments(cnt1)
    M2 = cv2.moments(cnt2)
    cx1 = int(M1["m10"] / M1["m00"])
    cy1 = int(M1["m01"] / M1["m00"])
    cx2 = int(M2["m10"] / M2["m00"])
    cy2 = int(M2["m01"] / M2["m00"])
    distance = np.sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)
    return distance

# Set the threshold distance for connecting contours
threshold_distance = 45

# Iterate over each contour
for contour1 in contours:
    # Calculate contour area
    contour_area = cv2.contourArea(contour1)

    # Skip contours with small area
    if contour_area < min_contour_area:
        continue

    # Approximate the contour with fewer points
    epsilon = 0.01 * cv2.arcLength(contour1, True)
    approx = cv2.approxPolyDP(contour1, epsilon, True)

    # Iterate over the remaining contours
    for contour2 in contours:
        # Skip the same contour or contours with small area
        if contour2 is contour1 or cv2.contourArea(contour2) < min_contour_area:
            continue

        # Calculate the distance between the contours
        distance = calculate_distance(approx, contour2)

        # Connect contours if they are close
        if distance < threshold_distance:
            # Draw a line or curve connecting the contours
            cv2.drawContours(image, [approx, contour2], -1, (0, 255, 0), 2)

# Display the image
cv2.imshow('DNA Segmentation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
