from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os

app = Flask(__name__)
model = load_model('models/cnn_model.h5')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def prepare_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        filename = secure_filename(file.filename)
        if filename == '':
            return "No file selected"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        print("Saved to:", filepath)
        print("Exists?", os.path.exists(filepath))


        img = prepare_image(filepath)
        prediction = model.predict(img)[0][0]

        if prediction > 0.5:
            label = "Fake"
            confidence = prediction
        else:
            label = "Real"
            confidence = 1 - prediction

        confidence = round(confidence * 100, 2)


        return render_template('result.html', label=label, confidence=confidence, filename=filename)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
