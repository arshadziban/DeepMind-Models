from flask import Flask, request, render_template
import torch
from PIL import Image
import numpy as np
from torchvision import transforms
import os
import torchvision.models as models

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = 'model_state.pth'  
num_classes = 2  


model = models.resnet18(pretrained=False)  
model.fc = torch.nn.Linear(model.fc.in_features, num_classes) 

# Load the state dictionary
model.load_state_dict(torch.load(model_path, map_location=device), strict=False)


model.to(device)
model.eval()

CLASS_NAMES = ["Ant", "Bee"]  
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize ((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        img_array = preprocess_image(file_path)

        with torch.no_grad():
            outputs = model(img_array)
            _, predicted = torch.max(outputs, 1)
            predicted_class = CLASS_NAMES[predicted.item()]

        os.remove(file_path)

        return render_template('index.html', prediction=predicted_class)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16 MB
    app.run(debug=True)