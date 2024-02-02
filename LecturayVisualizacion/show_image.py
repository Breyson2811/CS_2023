import cv2
import numpy as np

imagen = cv2.imread("unsa.jpg", 1)
cv2.imshow("Imagen Abierta", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
