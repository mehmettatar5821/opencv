import cv2
import numpy as np

img1 = cv2.imread("kizilelma.jpg")
img2 = cv2.imread("togg.jpg")



toplam = cv2.addWeighted(img1,0.3,img2,0.5,0)
cv2.imshow("resim",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()