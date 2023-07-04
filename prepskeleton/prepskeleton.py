from skimage.morphology import skeletonize
from skimage.util import invert
import cv2
import numpy as np
from data import *

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#Thresholding
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Invert the binary image
binary = invert(binary)

# Perform skeletonization
skeleton = skeletonize(binary)

# Convert back to BGR for displaying with OpenCV
skeleton_bgr = cv2.cvtColor((skeleton * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)

# Display the skeleton image
cv2.imshow('DNA Segmentation', skeleton_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
