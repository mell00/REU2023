import cv2
import numpy as np
import matplotlib.pyplot as plt


def impulse_size_based_median_filtering(img, threshold, window_size=5):
    # Get the padding size
    pad_size = window_size // 2

    # Pad the image with zeros
    img_padded = np.pad(img, pad_size, mode='constant')

    # Initialize an empty array to hold the filtered image
    filtered_img = np.zeros_like(img)

    # Iterate over the padded image
    for i in range(pad_size, img_padded.shape[0]-pad_size):
        for j in range(pad_size, img_padded.shape[1]-pad_size):
            # Calculate the median of the neighborhood
            median = np.median(img_padded[i-pad_size:i+pad_size+1, j-pad_size:j+pad_size+1])

            # If the pixel's value deviates from the median by more than the threshold,
            # replace it with the median; otherwise, leave it unchanged
            if np.abs(img_padded[i, j] - median) > threshold:
                filtered_img[i-pad_size, j-pad_size] = median
            else:
                filtered_img[i-pad_size, j-pad_size] = img_padded[i, j]

    return filtered_img
    
# Set the threshold
threshold = 30

# Apply the impulse size based median filtering
filtered_img = impulse_size_based_median_filtering(img, threshold, window_size=5)