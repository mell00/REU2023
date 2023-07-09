import cv2
import numpy as np
from data import *

def sharpen_image(image, strength=1, radius=1):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to create a blurred version of the image
    blurred = cv2.GaussianBlur(gray, (5, 5), radius)
    
    # Calculate the sharpened image by subtracting the blurred image from the original image
    sharpened = cv2.addWeighted(gray, 1 + strength, blurred, -strength, 0)
    
    # Convert the sharpened image back to color
    sharpened_image = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2BGR)
    
    return sharpened_image

# Load the original DNA strand image
image = cv2.imread('dna.jpg')

# Apply sharpening to the image
sharpened_image = sharpen_image(image, strength=1.5, radius=3)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
