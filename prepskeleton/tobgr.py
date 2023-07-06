import cv2
import numpy as np

# Assuming you have an image stored in the 'image' variable
# Make sure 'image' is a NumPy array representing the image

def toBgr(image):
	# Convert the image array to a byte buffer
	_, image_buffer = cv2.imencode('.jpg', image)

	# Decode the byte buffer into a BGR image
	bgr_image = cv2.imdecode(image_buffer, cv2.IMREAD_COLOR)

	return bgr_image