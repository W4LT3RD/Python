import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (13, 13), 0)
cv2.imshow("Imagen", image)

edged = cv2.Canny(image, 30, 150)
cv2.imshow("Edge", edged)
cv2.waitKey(0)