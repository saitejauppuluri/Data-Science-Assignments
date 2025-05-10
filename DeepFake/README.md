DEEPFAKE IMAGE CLASSIFIER — QUICK SETUP GUIDE
=============================================

STEP 1: Add Dataset
-------------------
Download the dataset from:
https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images

Place the folders (Train, Validation, Test) inside the 'Dataset' folder in this project.
The folder structure is already set — just copy the images in.

STEP 2: Open Project
--------------------
Open the entire project folder in Visual Studio Code.

STEP 3: Install Dependencies
----------------------------
Open a terminal in VS Code and run:

    pip install tensorflow opencv-python numpy matplotlib flask scikit-learn seaborn

(Make sure Python 3.10 or 3.11 is being used — TensorFlow may not work on 3.13+)

STEP 4: Run the Web App
-----------------------
In the terminal, run:

    python src/app.py

Then open your browser and go to:

    http://127.0.0.1:5000

Upload any image (jpg/png) and check the result!

(Optional)
----------
If you want to evaluate the model:

    python src/evaluate.py

If you want to retrain the model:

    python src/cnn_model.py 