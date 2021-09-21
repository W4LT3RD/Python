import cv2

img=cv2.imread('sol.jpg',0)

cv2.imshow("ImagenGris", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

