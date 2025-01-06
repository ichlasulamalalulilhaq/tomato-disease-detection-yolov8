import os
from collections import Counter
import matplotlib.pyplot as plt

# List folder anotasi YOLO
annotations_folders = [
    "D:/KULIAH/AI/DatasetTomat/test/labels",
    "D:/KULIAH/AI/DatasetTomat/train/labels",
    "D:/KULIAH/AI/DatasetTomat/valid/labels"
]

# Fungsi untuk membaca file label YOLO dan menghitung kelas
def check_class_balance(annotations_folders):
    overall_counter = Counter()
    folder_counters = {}

    for folder in annotations_folders:
        class_counter = Counter()
        
        # Iterasi file label dalam folder
        for label_file in os.listdir(folder):
            if label_file.endswith(".txt"):
                file_path = os.path.join(folder, label_file)
                with open(file_path, "r") as f:
                    # Baca setiap baris (format YOLO: class_id x_center y_center width height)
                    for line in f.readlines():
                        class_id = int(line.split()[0])  # Ambil class_id
                        class_counter[class_id] += 1
        
        # Simpan hasil per folder
        folder_counters[folder] = class_counter
        overall_counter.update(class_counter)

    # Cetak hasil distribusi kelas untuk setiap folder
    for folder, counter in folder_counters.items():
        total_instances = sum(counter.values())
        print(f"\nFolder: {folder}")
        print(f"Total instances: {total_instances}")
        for class_id, count in counter.items():
            percentage = (count / total_instances) * 100
            print(f"  Class {class_id}: {count} instances ({percentage:.2f}%)")
    
    # Cetak hasil keseluruhan
    print("\nOverall Distribution Across All Folders:")
    total_instances = sum(overall_counter.values())
    print(f"Total instances: {total_instances}")
    for class_id, count in overall_counter.items():
        percentage = (count / total_instances) * 100
        print(f"  Class {class_id}: {count} instances ({percentage:.2f}%)")
    
    return overall_counter, folder_counters

# Fungsi untuk visualisasi distribusi kelas
def plot_class_distribution(class_distribution, title="Class Distribution"):
    classes = list(class_distribution.keys())
    counts = list(class_distribution.values())
    
    plt.bar(classes, counts, color='skyblue')
    plt.xlabel("Class ID")
    plt.ylabel("Number of Instances")
    plt.title(title)
    plt.xticks(classes)  # Tampilkan ID kelas
    plt.show()

# Panggil fungsi untuk mengecek keseimbangan
overall_distribution, folder_distributions = check_class_balance(annotations_folders)

# Visualisasi hasil keseluruhan
plot_class_distribution(overall_distribution, title="Overall Class Distribution")
