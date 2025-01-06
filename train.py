from ultralytics import YOLO
import torch

# Cek apakah GPU tersedia
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Menggunakan perangkat {device}")

# Tentukan lokasi model YOLOv8 yang ingin digunakan
model = YOLO("yolov8n.yaml").to(device)  # Gunakan model konfigurasi .yaml

# Tentukan path ke file dataset.yaml Anda
dataset_path = "D:\\KULIAH\\AI\\DatasetTomat\\data.yaml"

# Tentukan jumlah workers berdasarkan jumlah core/logical processors
workers = 8  # Jumlah workers disesuaikan dengan jumlah core/CPU
batch_size = 4  # Sesuaikan batch size sesuai kapasitas GPU/CPU

# Latih model
model.train(
    data=dataset_path,
    epochs=500,
    imgsz=640,
    batch=batch_size,  # Batch size yang lebih kecil
    patience=50,  # Early stopping jika akurasi tidak meningkat setelah 50 epoch
    optimizer='AdamW',  # Gunakan optimizer Adam yang umumnya cepat konvergen
    lr0=1e-3,  # Awal learning rate
    augment=True,  # Aktifkan augmentasi dinamis
    val=True,  # Lakukan validasi setelah setiap epoch
    workers=workers,  # Tentukan jumlah workers untuk mempercepat pemrosesan data
)
