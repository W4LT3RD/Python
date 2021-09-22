import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (10, 10), 0)
cv2.imshow("Imagen", image)

edged = cv2.Canny(image, 30, 150)
cv2.imshow("Edge", edged)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print ("Contando la cantidad de monedas en la imagen: %d" % (len(cnts)))

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Monedas", coins)

for (i, c) in enumerate(cnts): 
    (x, y, w, h) = cv2.boundingRect(c)

    print(f"Monedas: {i+1}")
    coin = image[y:y + h, x:x +w]
    cv2.imshow

    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask=mask[y:y + h, x:x +w]
    cv2.imshow("Masked coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)
    