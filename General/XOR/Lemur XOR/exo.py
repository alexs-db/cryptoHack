import cv2
import numpy as np



# Read two images. The size of both images must be the same.
img1 = cv2.imread('lemur.png')
img2 = cv2.imread('flag.png')

# compute bitwise XOR on both images
xor_img = cv2.bitwise_xor(img1,img2)

# display the computed bitwise XOR image
cv2.imshow('Bitwise XOR Image', xor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()