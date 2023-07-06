import cv2
import numpy as np
from prepskeleton import *


# Invert the colors of the skeleton image
inverted_image = cv2.bitwise_not(skeleton)

# Display the result
cv2.imshow('Inverted Skeleton', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()