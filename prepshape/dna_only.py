
'''import cv2
import numpy as np
from prepshape import *

# Load the image
prepped_image = image
original_image = cv2.imread('dna.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(prepped_image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the green color range
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Threshold the HSV image to get only the green regions
mask = cv2.inRange(hsv, lower_green, upper_green)

# Perform morphological closing to fill gaps in the green regions
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

# Perform morphological opening to remove small particles inside the DNA structure
opened_mask = cv2.morphologyEx(closed_mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Apply the opened mask to the original image to get the DNA strand
dna_extracted = cv2.bitwise_and(original_image, original_image, mask=opened_mask)

# Create a white background image with the same size as the original image
white_background = np.full_like(original_image, (255, 255, 255))

# Create a mask for the DNA strand
dna_mask = cv2.cvtColor(dna_extracted, cv2.COLOR_BGR2GRAY)
_, dna_mask = cv2.threshold(dna_mask, 1, 255, cv2.THRESH_BINARY)

# Invert the DNA mask
dna_mask_inv = cv2.bitwise_not(dna_mask)

# Replace the background with white using the inverted DNA mask
result = cv2.bitwise_or(white_background, white_background, mask=dna_mask_inv)

# Combine the DNA extracted and the white background
result = cv2.bitwise_or(result, dna_extracted)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import cv2
import numpy as np
from prepshape import *

# Load the image
prepped_image = image
original_image = cv2.imread('dna.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(prepped_image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the green color range
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Threshold the HSV image to get only the green regions
mask = cv2.inRange(hsv, lower_green, upper_green)

# Perform morphological closing to fill gaps in the green regions
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
closed_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

# Perform morphological opening to remove small particles inside the DNA structure
opened_mask = cv2.morphologyEx(closed_mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Apply the opened mask to the original image to get the DNA strand
dna_extracted = cv2.bitwise_and(original_image, original_image, mask=opened_mask)

# Create a white background image with the same size as the original image
white_background = np.full_like(original_image, (255, 255, 255))

# Perform background subtraction
gray_image = cv2.cvtColor(dna_extracted, cv2.COLOR_BGR2GRAY)
_, foreground_mask = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY_INV)

# Replace the background with white using the foreground mask
result = cv2.bitwise_or(white_background, white_background, mask=foreground_mask)

# Combine the DNA extracted and the white background
result = cv2.bitwise_or(result, dna_extracted)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

