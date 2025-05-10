import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from collections import Counter
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import load_model
from data_generator import ImageDataGeneratorCV

model = load_model('models/cnn_model.h5')

test_gen = ImageDataGeneratorCV('Dataset/Test', batch_size=32, shuffle=False)

test_gen.indexes = np.arange(len(test_gen.filepaths))

y_true = test_gen.labels
y_pred_probs = model.predict(test_gen)
y_pred = (y_pred_probs > 0.5).astype(int).flatten()

cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Real', 'Fake'], yticklabels=['Real', 'Fake'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig('results/confusion_matrix.png')
plt.close()

print("Class counts:", Counter(y_true))
print("Classification Report:")
print(classification_report(y_true, y_pred, target_names=['Real', 'Fake'], labels=[0, 1]))

correct = []
incorrect = []

for i, (pred, true) in enumerate(zip(y_pred, y_true)):
    if pred == true and len(correct) < 5:
        correct.append(test_gen.filepaths[i])
    elif pred != true and len(incorrect) < 5:
        incorrect.append(test_gen.filepaths[i])
    if len(correct) == 5 and len(incorrect) == 5:
        break

def show_images(image_paths, title):
    plt.figure(figsize=(10, 2))
    for idx, img_path in enumerate(image_paths):
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, 5, idx + 1)
        plt.imshow(img)
        plt.axis('off')
    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(f'results/{title.replace(" ", "_").lower()}.png')
    plt.close()

show_images(correct, 'Correct Predictions')
show_images(incorrect, 'Incorrect Predictions')