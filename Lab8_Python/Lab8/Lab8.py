import cv2
import numpy as np

image = cv2.imread("E1R8HC-900x643.jpg")
cv2.imshow('E1R8HC-900x643.jpg', image)
cv2.waitKey(0)

b,g,r=cv2.split(image)
cv2.imshow("Model Blue Image", b)
cv2.imshow("Model Green Image", g)
cv2.imshow("Model Red Image", r)
cv2.waitKey(0)

image[:,:,1] = np.zeros([image.shape[0], image.shape[1]])
cv2.imshow('final image',image)
cv2.waitKey(0)