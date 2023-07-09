import cv2

ref_point = []
cropping = False

def click_and_drag(event, x, y, flags, param):
    # Declare global variables
    global ref_point, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False

        # Draw a rectangle around the ROI
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


# Load the image
image = cv2.imread("marble.jpg")
clone = image.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_drag)

while True:
    # Display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # Reset the image if the 'r' key is pressed
    if key == ord("r"):
        image = clone.copy()

    # Break the loop if the 'c' key is pressed
    elif key == ord("c"):
        break

# Perform cropping
cropped_image = image[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]

# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()
