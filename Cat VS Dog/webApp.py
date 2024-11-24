import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow Model Prediction
def model_prediction(test_image):
    # Load the pre-trained model
    model = tf.keras.models.load_model("cat_dog_classifier.h5")
    
    # Resize image to 128x128 (to match the model's training input size)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))  # Resize to 128x128
    input_arr = tf.keras.preprocessing.image.img_to_array(image)  # Convert image to array
    input_arr = input_arr / 255.0  # Normalize the image to match the model's training
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    
    return np.argmax(predictions)  # Return index of the maximum prediction value
 # Return index of the maximum prediction value

# Streamlit Application: Prediction Page
st.header("Model Prediction")

# Upload image
test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])

# Show uploaded image
if test_image is not None:
    st.image(test_image, use_container_width=True)

# Predict button
if st.button("Predict"):
    if test_image is not None:
        st.snow()  # Show a snowflake animation (optional)
        st.write("Our Prediction")
        
        # TensorFlow model expects a file path or file-like object
        result_index = model_prediction(test_image)
        
        # Reading Labels
        with open("labels.txt") as f:
            labels = [line.strip() for line in f.readlines()]
        
        # Display the predicted label
        st.success(f"Model is predicting it's a {labels[result_index]}")
    else:
        st.error("Please upload an image before predicting!")
