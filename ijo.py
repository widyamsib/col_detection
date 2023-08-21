import numpy as np
import cv2

# Inisialisasi video capture dari kamera (-1 untuk kamera default)
cap = cv2.VideoCapture(0)

while True:
    # Membaca frame dari video capture
    ret, frame = cap.read()

    # Ambil lebar dan tinggi dari frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Mengubah warna frame ke format HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Menentukan batas warna hijau(format HSV)
    lower_green = np.array([40, 40, 40])   #  batas bawah
    upper_green = np.array([80, 255, 255])  #  batas atas

    # BUat mask untuk warna hijau tetap dalam frame
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Buat result yang hanya akan menampilkan warna hijau
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Menampilkan result frame dan mask
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    # Keluar dari loop 
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
