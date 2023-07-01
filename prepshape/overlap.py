import cv2
import numpy as np
from shapely.geometry import LineString
from shapely.geometry import MultiLineString, MultiPoint, Point

def detect_intersections(points):
    line = LineString(points)
    if not line.is_simple:
        return line.intersection(line)
    return None

def mark_intersections(image, intersections, color=(0, 215, 0)):
    if intersections is None:
        return image

    if isinstance(intersections, MultiPoint):
        for point in intersections:
            image[int(point.y), int(point.x)] = color
    elif isinstance(intersections, MultiLineString):
        for line in intersections.geoms:
            for coord in line.coords:
                image[int(coord[1]), int(coord[0])] = color
    else:  # assuming it's a Point
        image[int(intersections.y), int(intersections.x)] = color

    return image

import cv2
import numpy as np

def intersect(segment1, segment2):
    """Check if two line segments intersect."""
    x1, y1, x2, y2 = segment1
    x3, y3, x4, y4 = segment2
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # lines are parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return (int(x), int(y))
    else:
        return None

# Load the mask here
# Assume the mask is a binary image where the DNA strands are white and the rest is black

# Find the contours of the DNA strands
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize an empty image to mark the intersections
intersection_image = np.zeros_like(mask)

# Iterate over each contour
for contour in contours:
    # Approximate the contour to a polygon
    polygon = cv2.approxPolyDP(contour, epsilon=3, closed=False)

    # Check each pair of line segments in the polygon for intersections
    num_points = len(polygon)
    for i in range(num_points):
        for j in range(i + 2, num_points):
            segment1 = (*polygon[i, 0], *polygon[(i + 1) % num_points, 0])
            segment2 = (*polygon[j, 0], *polygon[(j + 1) % num_points, 0])
            intersection = intersect(segment1, segment2)
            if intersection is not None:
                # Mark the intersection in the intersection image
                cv2.circle(intersection_image, intersection, radius=5, color=255, thickness=-1)

cv2.imshow('Intersections', intersection_image)
cv2.waitKey(0)
cv2.destroyAllWindows()





