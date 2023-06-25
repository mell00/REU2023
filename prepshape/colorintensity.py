import cv2
import numpy as np
from data import *


# Calculate the average pixel intensity
average_intensity = np.mean(gray)

# Define a threshold value to determine darkness or lightness
threshold = 127  # Adjust this value based on your requirements

# Check if the image has a dark background
if average_intensity < threshold:
    print("Image has a dark background")
else:
    print("Image has a light background")
