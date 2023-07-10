import numpy as np
from skimage.morphology import skeletonize
from skimage.util import invert
from skimage.transform import resize

def standardize_image_size(image, target_size):
    # Resize the image to the target size
    resized_image = resize(image, target_size, mode='constant')

    # Threshold the resized image to obtain a binary skeleton
    threshold = resized_image.mean()
    binary_image = resized_image > threshold

    # Skeletonize the binary image
    skeleton = skeletonize(binary_image)

    return skeleton

def skeleton_to_adjacency_matrix(skeleton, buffer_size=1):
    # Invert the skeleton image
    skeleton = invert(skeleton)

    # Get the coordinates of the skeleton pixels
    rows, cols = np.nonzero(skeleton)

    # Determine the size of the adjacency matrix with buffer
    num_pixels = len(rows)
    matrix_size = num_pixels + 2 * buffer_size

    # Initialize an empty adjacency matrix
    adjacency_matrix = np.zeros((matrix_size, matrix_size), dtype=int)

    # Iterate over the skeleton pixels
    for i in range(num_pixels):
        x1, y1 = cols[i], rows[i]

        # Check the neighbors of the current pixel
        for j in range(i + 1, num_pixels):
            x2, y2 = cols[j], rows[j]

            # Calculate the Euclidean distance between the pixels
            distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # If the distance is below a threshold, consider the pixels as connected
            if distance <= 1.5:
                adjacency_matrix[i + buffer_size, j + buffer_size] = 1
                adjacency_matrix[j + buffer_size, i + buffer_size] = 1

    return adjacency_matrix

# Example usage
skeleton_image = np.array([[0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 1, 0, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0]])

# Standardize the size of the skeleton image to (50, 50)
target_size = (50, 50)
standardized_image = standardize_image_size(skeleton_image, target_size)

adjacency_matrix = skeleton_to_adjacency_matrix(standardized_image, buffer_size=1)
print(adjacency_matrix)
