import os
import cv2
import numpy as np

def load_dataset(folder_path, label_map={'Fake': 1, 'Real': 0}, image_size=(128, 128), min_file_size=2_500, min_dims=(64, 64)):
    images = []
    labels = []

    for label_name, label in label_map.items():
        path = os.path.join(folder_path, label_name)
        for img_file in os.listdir(path):
            if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue  #skip unsupported file types

            img_path = os.path.join(path, img_file)
            
            #skip if file is too small (likely corrupt or empty)
            if os.path.getsize(img_path) < min_file_size:
                print(f"Skipping small file: {img_file}")
                continue
            
            try:
                img = cv2.imread(img_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                h, w, _ = img.shape

                #check for minimum dimensions
                if h < min_dims[0] or w < min_dims[1]:
                    print(f"Skipping small image: {img_file} ({w}x{h})")
                    continue

                img = cv2.resize(img, image_size)
                img = img.astype(np.float32) / 255.0

                images.append(img)
                labels.append(label)

            except Exception as e:
                print(f"Error loading {img_path}: {e}")

    return np.array(images), np.array(labels)

def save_datasets():
    base_path = 'Dataset'

    print("Processing Train...")
    X_train, y_train = load_dataset(os.path.join(base_path, 'Train'))
    np.save('X_train.npy', X_train)
    np.save('y_train.npy', y_train)

    print("Processing Validation...")
    X_val, y_val = load_dataset(os.path.join(base_path, 'Validation'))
    np.save('X_val.npy', X_val)
    np.save('y_val.npy', y_val)

    print("Processing Test...")
    X_test, y_test = load_dataset(os.path.join(base_path, 'Test'))
    np.save('X_test.npy', X_test)
    np.save('y_test.npy', y_test)

    print("Dataset saved successfully")
    print("Shapes:")
    print("Train:     ", X_train.shape, y_train.shape)
    print("Validation:", X_val.shape, y_val.shape)
    print("Test:      ", X_test.shape, y_test.shape)

if __name__ == "__main__":
    save_datasets()