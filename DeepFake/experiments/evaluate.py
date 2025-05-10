import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import cv2
from collections import Counter
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#paths
test_dir = "Dataset/Test"
model_path = "src/experiments/models/final_mobilenetv2.h5"
results_dir = "src/experiments/results"
os.makedirs(results_dir, exist_ok=True)

#load model
model = load_model(model_path)

#load validation set using generator
val_dir = "Dataset/Validation"

val_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    val_dir,
    target_size=(128, 128),
    batch_size=1,
    class_mode='binary',
    shuffle=False
)

#load all data into memory
X_val = []
y_true = []
filepaths = []

for i in range(len(val_gen.filenames)):
    img_path = os.path.join(val_dir, val_gen.filenames[i])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img.astype(np.float32) / 255.0
    X_val.append(img)
    y_true.append(val_gen.labels[i])
    filepaths.append(img_path)

X_val = np.array(X_val)
y_true = np.array(y_true)

#predict on all
y_pred_probs = model.predict(X_val).flatten()
y_pred = (y_pred_probs > 0.5).astype(int)

#confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Real', 'Fake'], yticklabels=['Real', 'Fake'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig(f"{results_dir}/confusion_matrix_final.png")
plt.close()

print("Class counts:", Counter(y_true))
print("Classification Report:")
print(classification_report(y_true, y_pred, target_names=['Real', 'Fake'], labels=[0, 1]))

fpr, tpr, _ = roc_curve(y_true, y_pred_probs)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], 'k--')
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.savefig(f"{results_dir}/roc_curve_final.png")
plt.close()

correct = []
incorrect = []

for i, (pred, true) in enumerate(zip(y_pred, y_true)):
    if pred == true and len(correct) < 5:
        correct.append(filepaths[i])
    elif pred != true and len(incorrect) < 5:
        incorrect.append(filepaths[i])
    if len(correct) == 5 and len(incorrect) == 5:
        break

def save_image_grid(paths, filename, title):
    plt.figure(figsize=(10, 2))
    for i, path in enumerate(paths):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(1, 5, i+1)
        plt.imshow(img)
        plt.axis('off')
    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, filename))
    plt.close()

save_image_grid(correct, "correct_predictions_final.png", "Correct Predictions")
save_image_grid(incorrect, "incorrect_predictions_final.png", "Incorrect Predictions")