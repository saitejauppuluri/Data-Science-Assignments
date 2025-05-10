import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, models
from data_generator import ImageDataGeneratorCV

'''
X_train = np.load('X_train.npy')
y_train = np.load('y_train.npy')

X_val = np.load('X_val.npy')
y_val = np.load('y_val.npy')
'''


train_gen = ImageDataGeneratorCV('Dataset/Train', batch_size=32)
val_gen = ImageDataGeneratorCV('Dataset/Validation', batch_size=32)

'''
train_gen.filepaths = train_gen.filepaths[:2000]
train_gen.labels = train_gen.labels[:2000]
train_gen.indexes = np.arange(len(train_gen.filepaths))

val_gen.filepaths = val_gen.filepaths[:1000]
val_gen.labels = val_gen.labels[:1000]
val_gen.indexes = np.arange(len(val_gen.filepaths))
'''

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=5
)

model.save('models/cnn_model.h5')

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()
plt.savefig('results/cnn_accuracy.png')
plt.close()