import cv2
import numpy as np

# 512x512 boyutlarında, 3 kanallı (RGB) siyah bir görüntü (tuval) oluşturuyoruz
canvas = np.zeros((512, 512, 3), dtype="uint8")

# 1. ÇİZGİ ÇİZME (Line)
# cv2.line(görüntü, başlangıç, bitiş, renk, kalınlık)
cv2.line(canvas, (0, 0), (512, 512), (255, 0, 0), 5) # Mavi çapraz çizgi

# 2. DİKDÖRTGEN ÇİZME (Rectangle)
# cv2.rectangle(görüntü, sol_üst, sağ_alt, renk, kalınlık)
# Kalınlık yerine -1 yazılırsa içi dolu olur
cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3) # Yeşil boş kare
cv2.rectangle(canvas, (300, 50), (450, 150), (0, 0, 255), -1) # Kırmızı dolu dikdörtgen

# 3. DAİRE ÇİZME (Circle)
# cv2.circle(görüntü, merkez, yarıçap, renk, kalınlık)
cv2.circle(canvas, (256, 256), 50, (255, 255, 0), 4) # Turkuaz daire

# 4. METİN EKLEME (PutText)
# cv2.putText(görüntü, metin, konum, font, ölçek, renk, kalınlık)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas, 'OpenCV Geometri', (10, 480), font, 1, (255, 255, 255), 2)

# 5. POLİGON (Çokgen) ÇİZME
# Köşe noktalarını belirliyoruz
pts = np.array([[100, 300], [200, 350], [150, 450], [50, 400]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], True, (0, 255, 255), 3) # Sarı çokgen

# Sonucu pencerede göster
cv2.imshow("Geometrik Sekiller", canvas)

# Bir tuşa basılana kadar bekle ve sonra pencereleri kapat
cv2.waitKey(0)
cv2.destroyAllWindows()