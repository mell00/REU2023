import cv2
import numpy as np
from PIL import Image
from data import *


def turn_white(gray):
    inverted_gray = invert_colors_gray(gray)
    # Display the image
    cv2.imshow('Inverted Image', inverted_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def invert_colors_gray(gray):
    # Convert the grayscale image to a PIL image
    gray_image = Image.fromarray(gray)

    # Invert the grayscale image using the bitwise NOT operator (~)
    inverted_gray = cv2.bitwise_not(gray)

    return inverted_gray



# Calculate the average pixel intensity
average_intensity = np.mean(gray)

# Define a threshold value to determine darkness or lightness
threshold = 127  # Adjust this value based on your requirements

# Check if the image has a dark background
if average_intensity < threshold:
    print("Image has a dark background")
    turn_white(gray)
else:
    print("Image has a light background")

    # Display the image
    cv2.imshow('Original Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Assuming you have a grayscale image stored in the 'gray' variable

