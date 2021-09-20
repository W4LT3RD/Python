import cv2
import numpy as np

print(cv2.__version__)
im = np.zeros((300,300,3), dtype=np.uint8)

cv2.imshow("Prueba", im)
cv2.waitKey(0)
