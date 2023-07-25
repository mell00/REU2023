'''import cv2
import numpy as np
from scipy.ndimage import generic_filter

def hysteresis_smoothing(image, threshold_low, threshold_high):
    # Apply hysteresis thresholding
    strong_pixels = (image >= threshold_high)
    weak_pixels = (image >= threshold_low) & (image < threshold_high)

    # Create an edge map to store the result
    edge_map = np.zeros_like(image, dtype=np.uint8)

    # Initialize the edge map with strong pixels
    edge_map[strong_pixels] = 1

    # Use a generic filter to find connected weak pixels
    def hysteresis_filter(values):
        return 1 if np.any(values) else 0

    new_edge_pixels = generic_filter(edge_map, hysteresis_filter, size=(3, 3))

    # Update the edge map with new weak pixels
    edge_map[tuple(new_edge_pixels.squeeze().T)] = 1

    return edge_map

def detect_faint_wrinkles(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define hysteresis thresholds (you can adjust these as needed)
    threshold_low = 1
    threshold_high = 3

    # Apply hysteresis smoothing to detect faint wrinkles
    edge_map = hysteresis_smoothing(image, threshold_low, threshold_high)

    return edge_map

if __name__ == "__main__":
    image_path = "grid3_dna_5700.jpg"  # Replace with the path to your image
    skeletonized_image = detect_faint_wrinkles(image_path)

    # Save the skeletonized image
    cv2.imwrite("skeletonized_image.jpg", (skeletonized_image * 255).astype(np.uint8))'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('grid3_dna_5700.jpg', 0)

# Set filter strength (10 is a good starting point)
filter_strength = 3000

# Apply Non-Local Means Denoising
filtered_img = cv2.fastNlMeansDenoising(img, None, filter_strength, 7, 21)

# Create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img = clahe.apply(filtered_img)

#Apply morphological operations to enhance the creases
kernel = np.ones((10,10), np.uint8)
morph_img = cv2.morphologyEx(clahe_img, cv2.MORPH_OPEN, kernel)


# Perform binary thresholding to create a mask of the lines
_, mask = cv2.threshold(morph_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Invert the mask
mask_inv = cv2.bitwise_not(mask)

# Create an image of the desired background color
background_color = 255
background = np.full_like(img, background_color)

# Apply the inverted mask to the background image
img_lines_on_background = np.where(mask_inv == 255, img, background)

# Display the original, denoised, CLAHE, Morphed and Thresholded images for comparison
plt.figure(figsize=(24,6))
#plt.subplot(151), plt.imshow(img, cmap='gray'), plt.title('Original')
#plt.subplot(152), plt.imshow(filtered_img, cmap='gray'), plt.title('Denoised')
plt.subplot(151), plt.imshow(clahe_img, cmap='gray'), plt.title('CLAHE Enhanced')
#plt.subplot(154), plt.imshow(morph_img, cmap='gray'), plt.title('Morphology Enhanced')
plt.subplot(152), plt.imshow(mask, cmap='gray'), plt.title('Mask')
plt.subplot(153), plt.imshow(img_lines_on_background, cmap='gray'), plt.title('Lines on Background')
plt.show()










