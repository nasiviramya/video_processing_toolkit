import cv2
import numpy as np

# Paths to your input images
img1_path = "input1.jpg"
img2_path = "input2.jpg"

# Read the images
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Check if images are same height
if img1.shape[0] != img2.shape[0]:
    # Resize second image to match first image's height
    h = img1.shape[0]
    w = int(img2.shape[1] * (h / img2.shape[0]))
    img2 = cv2.resize(img2, (w, h))

# Combine horizontally (side by side)
combined = np.hstack((img1, img2))

# Save and show result
cv2.imwrite("combined.jpg", combined)
cv2.imshow("Combined Image", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
