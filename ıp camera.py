import cv2

url = "http://192.168.0.26.8080/video"#burada indirdiğiniz ip kamera uygulamasındaki ıp girmeniz gerekmektedir 

cam = cv2.VideoCapture(url)

while cam.isOpened():
    ret, frame = cam.read()

    if not ret:
        print("kameradan görüntü okunamadı")

    cv2.imshow("görüntü",frame)

    if cv2.waitKey(1) == ord("q"):

cv2.destroyAllWindows()