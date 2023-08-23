import numpy as np
import cv2

# Inisialisasi video capture dari file video
cap = cv2.VideoCapture("D:\Iwang Mine\P1-COL\FOREST.mp4")

# Ambil lebar dan tinggi dari frame
width = int(cap.get(3))
height = int(cap.get(4))
frame_rate = 25

# Mendefinisikan codec dan pembuat video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec untuk format video
out = cv2.VideoWriter('output.avi', fourcc, frame_rate, (width, height))

while True:
    # Membaca frame dari video capture
    ret, frame = cap.read()

    # Mengubah warna frame ke format HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Menentukan batas warna hijau (format HSV)
    lower_green = np.array([40, 40, 40])   # Batas bawah
    upper_green = np.array([80, 255, 255])  # Batas atas

    # Buat mask untuk warna hijau tetap dalam frame
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Buat result yang hanya akan menampilkan warna hijau
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Menulis frame yang telah diproses ke video
    out.write(result)

    # Menampilkan frame yang telah diproses
    cv2.imshow('frame', result)

    # Keluar dari loop
    if cv2.waitKey(1) == ord('q'):
        break


# Menutup objek VideoWriter dan VideoCapture
out.release()
cap.release()
