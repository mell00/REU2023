import cv2
import numpy as np
from scipy.interpolate import make_interp_spline
from prepshape import *

def count_dna_contours(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to obtain a binary image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of contours
    num_contours = len(contours)

    # Print the result
    print("Number of contours: ", num_contours)

# Example usage: Specify the path to the image
image_path = 'dna_image.jpg'  # Replace with the actual image file path

count_dna_contours(image_path)
