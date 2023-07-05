import cv2
import numpy as np
from scipy.interpolate import splprep, splev
from prepskeleton import *
from skeletonintersection import *
import os

def draw_largest_contours(image, mask, min_contour_length):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on length
    large_contours = [cnt for cnt in contours if cv2.arcLength(cnt, True) > min_contour_length]

    if not large_contours:
        raise ValueError("No large contours found")
    
    contour_image = cv2.drawContours(image.copy(), large_contours, -1, (0, 255, 0), 2)
    return contour_image, large_contours

def fit_curve_to_contours(large_contours):
    points = np.vstack([contour.squeeze() for contour in large_contours])
    x, y = points[:, 0], points[:, 1]
    tck, u = splprep([x, y], s=0, per=1)
    u_new = np.linspace(u.min(), u.max(), 1000)
    x_new, y_new = splev(u_new, tck)
    return np.column_stack((x_new, y_new)).astype(np.int32)

def main():
    min_contour_area = 5  # Set your minimum contour area
    
    # Assuming skeleton_mask is your binary mask after skeletonization
    # It should be a binary image where the skeletons are white (255) and the background is black (0)
    skeleton_mask = skeleton
    contour_image, large_contours = draw_largest_contours(image, skeleton_mask, min_contour_area)
    curve_points = fit_curve_to_contours(large_contours)
    #intersections = detect_intersections(curve_points)
    nurbs_image = cv2.polylines(contour_image.copy(), [curve_points], isClosed=False, color=(0, 0, 255), thickness=2)
    #marked_image = mark_intersections(nurbs_image, intersections)
    cv2.imshow('Original Image', image)
    cv2.imshow('Contour Image', contour_image)
    #cv2.imshow('NURBS Image', marked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
