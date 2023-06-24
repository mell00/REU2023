import cv2
import numpy as np

# Load the electron microscope image
image = cv2.imread('dna.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform histogram equalization to enhance contrast
equalized = cv2.equalizeHist(blurred)

# Adaptive thresholding to obtain a binary image
adaptive_threshold = cv2.adaptiveThreshold(equalized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Opening operation to remove noise and small structures
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(adaptive_threshold, cv2.MORPH_OPEN, kernel, iterations=2)

# Closing operation to fill gaps and smooth DNA regions
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=2)

# Dilation to further fill gaps and connect nearby DNA regions
dilated = cv2.dilate(closed, kernel, iterations=2)  # Increase the iterations

# find contours and filter based on area
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]  # Adjust the area threshold as needed

# create blank mask image
mask = np.zeros_like(gray)

# draw filtered contours on the mask
cv2.drawContours(mask, filtered_contours, -1, 255, thickness=cv2.FILLED)

# mask original image
result = cv2.bitwise_and(image, image, mask=mask)

# bilateral Filtering
denoised = cv2.bilateralFilter(result, d=9, sigmaColor=75, sigmaSpace=75)


# Display
cv2.imshow('Preprocessed Image', opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
