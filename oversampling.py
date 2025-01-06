import os
import shutil
import random

def oversample_class(label_folder, image_folder, class_id, target_count):
    files = [f for f in os.listdir(label_folder) if f.endswith(".txt")]
    class_files = []
    
    for file in files:
        with open(os.path.join(label_folder, file), "r") as f:
            if any(line.startswith(f"{class_id} ") for line in f.readlines()):
                class_files.append(file)

    current_count = len(class_files)
    if current_count >= target_count:
        print(f"Class {class_id} already has sufficient samples: {current_count}")
        return
    
    print(f"Oversampling Class {class_id}: {current_count} -> {target_count}")
    while len(class_files) < target_count:
        selected_file = random.choice(class_files)
        # Copy label file
        src_label = os.path.join(label_folder, selected_file)
        dst_label = os.path.join(label_folder, f"copy_{len(class_files)}_{selected_file}")
        shutil.copy(src_label, dst_label)

        # Copy corresponding image file
        src_image = os.path.join(image_folder, selected_file.replace(".txt", ".jpg"))
        dst_image = os.path.join(image_folder, f"copy_{len(class_files)}_{selected_file.replace('.txt', '.jpg')}")
        shutil.copy(src_image, dst_image)

        class_files.append(selected_file)


# Oversample folder Test
test_label_folder = "D:/KULIAH/AI/DatasetTomat/test/labels"
test_image_folder = "D:/KULIAH/AI/DatasetTomat/test/images"
oversample_class(test_label_folder, test_image_folder, class_id=0, target_count=69)
oversample_class(test_label_folder, test_image_folder, class_id=3, target_count=69)
oversample_class(test_label_folder, test_image_folder, class_id=4, target_count=69)
oversample_class(test_label_folder, test_image_folder, class_id=2, target_count=69)

# Oversample folder Train
train_label_folder = "D:/KULIAH/AI/DatasetTomat/train/labels"
train_image_folder = "D:/KULIAH/AI/DatasetTomat/train/images"
oversample_class(train_label_folder, train_image_folder, class_id=0, target_count=1361)
oversample_class(train_label_folder, train_image_folder, class_id=3, target_count=1361)
oversample_class(train_label_folder, train_image_folder, class_id=4, target_count=1361)
oversample_class(train_label_folder, train_image_folder, class_id=2, target_count=1361)

# Oversample folder Valid
valid_label_folder = "D:/KULIAH/AI/DatasetTomat/valid/labels"
valid_image_folder = "D:/KULIAH/AI/DatasetTomat/valid/images"
oversample_class(valid_label_folder, valid_image_folder, class_id=0, target_count=142)
oversample_class(valid_label_folder, valid_image_folder, class_id=3, target_count=142)
oversample_class(valid_label_folder, valid_image_folder, class_id=4, target_count=142)
oversample_class(valid_label_folder, valid_image_folder, class_id=2, target_count=142)
