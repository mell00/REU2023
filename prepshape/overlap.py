import cv2
import numpy as np
from seg import *

# Load the DNA image
image = cv2.imread("dna_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize the overlap count
overlap_count = 0

# Iterate over each contour
for i in range(len(contours)):
    contour1 = contours[i]

    for j in range(i + 1, len(contours)):
        contour2 = contours[j]

        # Check if the contours overlap
        intersection = cv2.bitwise_and(contour1, contour2)
        if cv2.countNonZero(intersection) > 0:
            overlap_count += 1

# Print the total overlap count
print("Total overlap count:", overlap_count)
