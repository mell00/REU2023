import cv2
import numpy as np

# Load the image
image = cv2.imread('./grid3_dna_5700.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)