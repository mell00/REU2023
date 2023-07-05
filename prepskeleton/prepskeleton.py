from skimage.morphology import skeletonize
from skimage.util import invert
from skimage.util import img_as_ubyte
import cv2
import numpy as np
from data import *

min_size = 10

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform thresholding to obtain a binary image
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Skeletonize the binary image
skeleton = skeletonize(binary / 255)

# Convert skeleton back to 8-bit image
skeleton = img_as_ubyte(skeleton)

from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

# Convert binary image to boolean
skeleton_bool = skeleton.astype(bool)

# Remove objects smaller than the minimum size
skeleton_bool = remove_small_objects(skeleton_bool, min_size, connectivity=2)

# Convert boolean image back to 8-bit
skeleton = img_as_ubyte(skeleton_bool)

# Display the image
cv2.imshow('DNA Segmentation', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()


