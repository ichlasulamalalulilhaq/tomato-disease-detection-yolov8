# tomato-disease-detection-yolov8
Proyek deteksi penyakit pada tanaman tomat menggunakan YOLOv8. Bahasa: Python, Framework: PyTorch, YOLOv8.

# Tomato Disease Detection using YOLOv8
Proyek ini bertujuan untuk memantau dan mencegah penyakit pada tanaman tomat (Solanum lycopersicum) dalam pertanian organik dengan menggunakan algoritma YOLOv8. Sistem ini memungkinkan deteksi penyakit tanaman tomat secara otomatis melalui analisis gambar, sehingga petani atau peneliti dapat mengidentifikasi kondisi tanaman dan mengambil tindakan yang tepat.

## Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python  
- **Framework**: PyTorch, YOLOv8  

## Fitur Utama
- Deteksi penyakit tanaman tomat secara otomatis berdasarkan gambar menggunakan model YOLOv8. 
- Hasil deteksi dapat digunakan untuk analisis lebih lanjut atau integrasi dengan sistem pemantauan pertanian.
- Dapat digunakan pada perangkat keras atau sistem pemrosesan gambar untuk pemantauan lapangan.

## Dataset
https://universe.roboflow.com/letspro-uvmvg/tomato-w4fvj/dataset/3

## Instalasi

#### 1. Clone Repository
```bash
git clone https://github.com/ichlasulamalalulilhaq/tomato-disease-detection-yolov8.git
cd tomato-disease-detection-yolov8
```

#### 2. Instal dependensi
Pastikan Anda sudah menginstal Python versi 3.8 atau lebih baru. Kemudian jalankan:
```bash
pip install -r requirements.txt
```

#### 3. Download Dataset
Unduh dataset dari link di atas, lalu masukkan ke folder proyek jika diperlukan.

## Cara Penggunaan

#### 1. Melatih Model
Jalankan perintah berikut untuk melatih model dengan dataset Anda:
```bash
python train.py
```

## Struktur Proyek

- **train.py**: Skrip untuk melatih model YOLOv8 dengan dataset.
- **oversampling.py**: Skrip untuk menangani dataset tidak seimbang dengan teknik oversampling.
- **balance_analysis.py**: Skrip untuk analisis keseimbangan data.
- **LICENSE**: Informasi lisensi proyek.
- **README.md**: Dokumentasi proyek.
- **Artikel Tomato Disease Detection YoloV8.pdf**: Artikel tentang proyek ini.
  




