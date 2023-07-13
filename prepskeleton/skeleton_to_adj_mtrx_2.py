import cv2
import numpy as np
from scipy.sparse import dok_matrix
from sklearn.feature_extraction import image
from prepskeleton import skeleton

# Load the skeleton image
skeleton_image = skeleton

# Threshold the skeleton image to obtain a binary representation
_, binary_image = cv2.threshold(skeleton_image, 127, 255, cv2.THRESH_BINARY)

# Convert the binary image to graph representation
graph = image.img_to_graph(binary_image)

# Convert the graph to adjacency matrix
adjacency_matrix = image.img_to_graph(binary_image, return_as=np.ndarray)

all_zeros = not adjacency_matrix.any()

# Print the adjacency matrix
print(adjacency_matrix)

print(all_zeros)
