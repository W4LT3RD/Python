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

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print ("Contando la cantidad de monedas en la imagen: %d" % (len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Monedas", coins)
cv2.waitKey(0)