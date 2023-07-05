import cv2
import numpy as np

# Load the image
image = cv2.imread('./dna.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)