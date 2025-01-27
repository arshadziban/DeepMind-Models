# Potato Disease Classification

This project implements a deep learning-based solution for classifying potato diseases using images. The model is built with TensorFlow and Keras, utilizing a Convolutional Neural Network (CNN) to classify potato leaf images into various disease categories.

## Project Overview

The goal of this project is to classify potato leaf images into healthy and diseased categories. The model is trained using the **PlantVillage Dataset**, which contains labeled images of various plant diseases.

## Dataset

The dataset used for training and validation is sourced from the [PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village), which includes images of plant diseases, including potato diseases. The dataset is split into three subsets:

- **80%** for training
- **10%** for validation
- **10%** for testing

## Features

- **Dataset Handling**: The dataset is preprocessed and split into training, validation, and test sets.
- **Image Preprocessing**: Images are resized to 256x256 pixels, normalized, and augmented to improve model generalization.
- **Model Architecture**: A Convolutional Neural Network (CNN) with:
  - Three convolutional layers
  - Two dense layers
- **Evaluation**: The training and validation accuracy/loss are plotted over epochs. The final model is evaluated on the test set to compute accuracy and loss metrics.

## Requirements

- Python 3.x
- TensorFlow
- Keras
- NumPy
- Matplotlib

You can install the required libraries using:

```bash
pip install tensorflow numpy matplotlib
```

## How It Works

1. **Image Upload**: Users upload an image of a potato leaf through the web application.
2. **Image Preprocessing**: The image is resized and normalized to match the input shape required by the model.
3. **Prediction**: The preprocessed image is passed through the trained model to predict the class label.
4. **Result Display**: The predicted class label is displayed on the web interface.

## Project Files

- `app.py`: Flask application code for deploying the model.
- `plant_disease_model.h5`: Pre-trained model file.
- `plant_disease_web_app.html`: HTML template for the web interface.
- `uploads/`: Temporary storage for uploaded images.
