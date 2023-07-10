"""
==============
Blob Detection
==============

Blobs are bright on dark or dark on bright regions in an image. In
this example, blobs are detected using 3 algorithms. The image used
in this case is the Hubble eXtreme Deep Field. Each bright dot in the
image is a star or a galaxy.

Laplacian of Gaussian (LoG)
-----------------------------
This is the most accurate and slowest approach. It computes the Laplacian
of Gaussian images with successively increasing standard deviation and
stacks them up in a cube. Blobs are local maximas in this cube. Detecting
larger blobs is especially slower because of larger kernel sizes during
convolution. Only bright blobs on dark backgrounds are detected. See
:py:meth:`skimage.feature.blob_log` for usage.

Difference of Gaussian (DoG)
----------------------------
This is a faster approximation of LoG approach. In this case the image is
blurred with increasing standard deviations and the difference between
two successively blurred images are stacked up in a cube. This method
suffers from the same disadvantage as LoG approach for detecting larger
blobs. Blobs are again assumed to be bright on dark. See
:py:meth:`skimage.feature.blob_dog` for usage.

Determinant of Hessian (DoH)
----------------------------
This is the fastest approach. It detects blobs by finding maximas in the
matrix of the Determinant of Hessian of the image. The detection speed is
independent of the size of blobs as internally the implementation uses
box filters instead of convolutions. Bright on dark as well as dark on
bright blobs are detected. The downside is that small blobs (<3px) are not
detected accurately. See :py:meth:`skimage.feature.blob_doh` for usage.
"""

from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
from prepskeleton import *

import matplotlib.pyplot as plt

def remove_blob_overlaps(image, blobs, skeleton):
    filtered_blobs = []
    mask = np.zeros_like(image, dtype=bool)

    for blob in blobs:
        y, x, r = blob

        # Define the region of the blob
        min_row = max(int(y - r), 0)
        max_row = min(int(y + r), image.shape[0] - 1)
        min_col = max(int(x - r), 0)
        max_col = min(int(x + r), image.shape[1] - 1)

        # Check if the region overlaps with any existing blobs or skeleton
        if np.any(mask[min_row:max_row, min_col:max_col]) or np.any(skeleton[min_row:max_row, min_col:max_col]):
            continue

        # Mark the region as occupied
        mask[min_row:max_row, min_col:max_col] = True

        # Add the blob to the filtered blobs
        filtered_blobs.append(blob)

    return np.array(filtered_blobs)





image_gray = skeleton

# Assuming 'skeleton' is your skeletonized image
rows, cols = np.nonzero(image_gray)
x1 = np.min(cols)
y1 = np.min(rows)
x2 = np.max(cols)
y2 = np.max(rows)

# Create a mask to exclude the DNA strand region
# Adjust the rectangle parameters to define the region more accurately
margin = 10
mask = np.zeros_like(image_gray, dtype=np.uint8)
cv2.rectangle(mask, (x1 - margin, y1 - margin), (x2 + margin, y2 + margin), 255, thickness=cv2.FILLED)

# Apply the mask to the image
image_gray_masked = cv2.bitwise_and(image_gray, mask)

blobs_log = blob_log(image_gray_masked, max_sigma=30, num_sigma=10, threshold=.1)

# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

blobs_dog = blob_dog(image_gray_masked, max_sigma=30, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

blobs_doh = blob_doh(image_gray_masked, max_sigma=30, threshold=.01)

blobs_list = [blobs_log, blobs_dog, blobs_doh]
colors = ['yellow', 'lime', 'red']
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(image_gray_masked)

    # Remove blobs that overlap with the skeleton
    filtered_blobs = remove_blob_overlaps(image_gray, blobs, skeleton)

    for blob in filtered_blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()

plt.tight_layout()
plt.show()
