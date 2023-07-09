import numpy as np
from skimage import io, measure
from prepskeleton import *

def get_3d_coordinates(image_stack):
    """
    Get the 3D coordinates of all non-zero pixels in an image stack.

    Parameters
    ----------
    image_stack : array-like
        An NxMxP array-like object where N, M, and P are the dimensions of the images.

    Returns
    -------
    coords : array-like
        A Qx3 array where Q is the number of non-zero pixels and each row is a 3D coordinate.
    """
    # Use np.nonzero to get the coordinates of all non-zero pixels
    coords = np.nonzero(image_stack)
    # np.nonzero returns a tuple of 1D arrays, so we need to stack them into a 2D array
    coords = np.column_stack(coords)
    return coords

def write_knotplot_file(points, filename):
    """
    Write a set of points to a file in KnotPlot's RMO format.

    Parameters
    ----------
    points : array-like
        An Nx3 array-like object where each row represents a point in 3D space.
    filename : str
        The path to the file to write.
    """
    with open(filename, 'w') as f:
        f.write(f'{len(points)}\n')  # Write the number of points
        for point in points:
            f.write(' '.join(map(str, point)) + '\n')  # Write the coordinates of each point

# Load the image stack (replace 'path_to_image_stack' with the path to your image stack)
image_stack = io.imread('path_to_image_stack')

# Get the 3D coordinates
coords = get_3d_coordinates(image_stack)

# Write these points to an RMO file
write_knotplot_file(coords, 'dna_strand.rmo')
