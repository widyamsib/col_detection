import numpy as np
import cv2

cap = cv2.VideoCapture(-1)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Batas warna hijau dalam format HSV
    lower_green = np.array([40, 40, 40])   # Nilai batas bawah
    upper_green = np.array([80, 255, 255])  # Nilai batas atas

    mask = cv2.inRange(hsv, lower_green, upper_green)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()