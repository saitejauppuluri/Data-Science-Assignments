import os
import cv2
import numpy as np
from tensorflow.keras.utils import Sequence

class ImageDataGeneratorCV(Sequence):
    def __init__(self, folder_path, label_map={'Fake': 1, 'Real': 0}, image_size=(128, 128), batch_size=32, shuffle=True):
        self.image_size = image_size
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.label_map = label_map
        self.filepaths, self.labels = self._load_filepaths(folder_path)
        self.indexes = np.arange(len(self.filepaths))
        self.on_epoch_end()

    def _load_filepaths(self, folder_path):
        filepaths = []
        labels = []
        for label_name, label in self.label_map.items():
            full_path = os.path.join(folder_path, label_name)
            for fname in os.listdir(full_path):
                if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
                    filepaths.append(os.path.join(full_path, fname))
                    labels.append(label)
        return filepaths, labels

    def __len__(self):
        return int(np.ceil(len(self.filepaths) / self.batch_size))

    def __getitem__(self, index):
        batch_indices = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        batch_filepaths = [self.filepaths[i] for i in batch_indices]
        batch_labels = [self.labels[i] for i in batch_indices]

        images = []
        for path in batch_filepaths:
            img = cv2.imread(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, self.image_size)
            img = img.astype(np.float32) / 255.0
            images.append(img)

        return np.array(images), np.array(batch_labels)

    def on_epoch_end(self):
        if self.shuffle:
            self.indexes = np.arange(len(self.filepaths))
            np.random.shuffle(self.indexes)