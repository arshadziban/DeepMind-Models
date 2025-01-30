# Ant and Bee Image Classification

## Overview
This project implements an image classification model to distinguish between images of ants and bees using a deep learning approach. The model is built using PyTorch and ResNet18 and is deployed as a web application using Flask.

## Features
- Binary classification of ants and bees.
- Utilizes ResNet18 for feature extraction.
- Web-based interface for easy image uploads and classification.
- Performance evaluation using accuracy and loss metrics.

## Technologies Used
- Python
- PyTorch
- Flask
- Torchvision (ResNet18 model)
- PIL (Pillow) for image processing
- HTML/CSS (for the web interface)

## Model Details
- The model uses ResNet18, a pre-trained deep learning model.
- The fully connected layer is modified to classify two categories: Ant and Bee.
- The model weights are loaded from `model_state.pth`.

## Dataset
Dataset Link: [Kaggle - Ants and Bees](https://www.kaggle.com/datasets/gauravduttakiit/ants-bees)
The dataset consists of images of ants and bees, preprocessed and augmented to enhance model performance.
