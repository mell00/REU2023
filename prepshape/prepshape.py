import cv2
import numpy as np

# Load the image
image = cv2.imread('./dna.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
cv2.destroyAllWindows()
