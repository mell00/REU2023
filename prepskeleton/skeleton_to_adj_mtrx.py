import cv2
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from skimage.morphology import skeletonize
from skimage.util import invert
from skimage.transform import resize
from prepskeleton import *

def standardize_image_size(image, target_size):
    # Normalize the image to [0, 1] range before resizing
    normalized_image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    
    # Resize the image to the target size
    resized_image = resize(normalized_image, target_size, mode='constant')

    # Threshold the resized image to obtain a binary skeleton
    threshold = resized_image.mean()
    binary_image = resized_image > threshold

    # Skeletonize the binary image
    skeleton = skeletonize(binary_image)

    return skeleton

def skeleton_to_adjacency_matrix(skele):
    # Invert the skeleton image
    inverted_image = invert(skele)

    # Resize the inverted image to match the size of the skeleton image
    resized_image = resize(inverted_image, skele.shape, mode='constant')

    # Threshold the resized image to obtain a binary image
    threshold = resized_image.mean()
    binary_image = resized_image > threshold

    # Find connected components in the binary image
    num_labels, labels = connected_components(binary_image, connectivity=2)

    # Create an empty adjacency matrix
    adjacency_matrix = csr_matrix((num_labels, num_labels), dtype=np.int8)

    # Iterate over each pixel in the skeleton image
    height, width = skele.shape
    for y in range(height):
        for x in range(width):
            if skele[y, x]:
                # Check the neighboring pixels
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height and skele[ny, nx]:
                        # Add an edge between the current pixel and the neighboring pixel
                        adjacency_matrix[labels[y, x], labels[ny, nx]] = 1

    all_zeros = not adjacency_matrix.nnz

    return adjacency_matrix, all_zeros

    # Print the adjacency matrix

    standardized_image = standardize_image_size(skeleton) 

    adjacency_matrix, is_zeros = skeleton_to_adjacency_matrix(standardized_image)

    print(adjacency_matrix)

    print(all_zeros)
