from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())
 
def plot_histograma(image, title, mask=None):
    chans = cv2.split(image)
    colors=("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
image=cv2.imread(args["image"])
cv2.imshow("Original",image)
plot_histograma(image, "Histograma de Imagen original")

mask = np.zeros(image.shape[:2], dtype="unit8")
cv2.rectangle(mask, (15,15), (130, 100), 255, -1)
cv2.imshow("Máscara", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Aplicando la máscara", masked) 

plot_histograma(image, "Histograma para la máscara de la imagen", mask=mask)

plt.show()
cv2.waitKey(0)

