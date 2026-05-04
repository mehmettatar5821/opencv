import cv2
import numpy as np

# 500x500 siyah bir zemin oluştur (Sen istersen kendi resmini cv2.imread ile oku)
img = np.zeros((500, 500, 3), np.uint8)

# Resmin içine bir dikdörtgen çizelim (ROI olarak seçeceğimiz yer belli olsun)
# (x1, y1) -> (x2, y2)
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), -1) # Yeşil bir kare

# --- ROI ALMA (Kesme) ---
# Formül: resim[y1:y2, x1:x2]
# Dikkat: Önce Y ekseni (satırlar), sonra X ekseni (sütunlar) yazılır.
roi = img[50:150, 50:150]

# --- ROI YAPIŞTIRMA ---
# Kestiğimiz bu 100x100'lük parçayı resmin başka bir yerine (mesela 300,300 koordinatına) koyalım
# Önemli: Yapıştırılacak alanın boyutu, ROI boyutuyla birebir aynı olmalı.
img[300:400, 300:400] = roi

# Sonuçları göster
cv2.imshow("Ana Resim", img)
cv2.imshow("Sadece ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()