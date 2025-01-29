from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained model
MODEL_PATH = "C:\\Users\\Arshad Ziban\\Desktop\\Skills\\Deep Learning\\Digit_Prediction\\digits_predict_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class names (corresponding to your training data)
CLASS_NAMES = [
    "0", "1",
    "2", "3", "4",
    "5", "6", "7",
    "8", "9"
]
 
# Helper function to process image
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256))  # Adjust size based on model input
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def home():
    return render_template('digit_prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save the uploaded file to a temporary location
    try:
        file_path = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        # Preprocess the image
        img_array = preprocess_image(file_path)

        # Predict the class
        predictions = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]

        # Clean up temporary file
        os.remove(file_path)

        return jsonify({"class": predicted_class})

    except Exception as e:
        # Log the exception and return the error message
        print(f"Error during prediction: {e}")
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == '__main__':
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16 MB
    app.run(debug=True)
