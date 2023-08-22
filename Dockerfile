# Gunakan image Python sebagai base image
FROM python:3.11.4

# Set working directory
WORKDIR /app

# Salin kode Python ke dalam container
COPY ijo.py .

# Instal OpenCV
RUN pip install opencv-python-headless

# Perintah default yang akan dijalankan ketika container dijalankan
CMD ["python", "ijo.py"]
# CMD ["bash"]