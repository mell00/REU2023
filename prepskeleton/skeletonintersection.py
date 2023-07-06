

import numpy as np
from data import *
from prepskeleton import *
from skimage.morphology import skeletonize
from skimage.util import invert
from skimage.util import img_as_ubyte
from scipy.ndimage import convolve
from skan.csr import skeleton_to_csgraph
from skan import Skeleton, summarize
from skan import draw



def find_neighbours(x, y, image):
    """Return 8-neighbours of image point P1(x,y), in a counter-clockwise order"""
    img = image
    x1, y1, x_1, y_1 = x+1, y+1, x-1, y-1
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1], 
             img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]

def getSkeletonIntersection(skeleton):
    """ Given a skeletonised image, it will give the coordinates of the intersections of the skeleton.
    
    Keyword arguments:
    skeleton -- the skeletonised image to detect the intersections of
    
    Returns: 
    List of 2-tuples (x,y) containing the intersection coordinates
    """
    # Create a copy of the skeleton
    image = skeleton.copy()
    # Normalize the image
    image = image / 255

    intersections = list()
    
    # Traverse the image
    for x in range(1, image.shape[0] - 1):
        for y in range(1, image.shape[1] - 1):
            # If we have a white pixel
            if image[x][y] == 1:
                # Get the neighbours
                neighbours = find_neighbours(x, y, image)
                # If the pixel is an intersection
                if sum(neighbours) > 2:
                    intersections.append((y, x))

    return intersections
