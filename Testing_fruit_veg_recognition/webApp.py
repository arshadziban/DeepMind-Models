import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow Model Prediction
def model_prediction(test_image):
    # Load the pre-trained model
    model = tf.keras.models.load_model("trained_model.h5")
    # Load and preprocess the image
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # Return index of the maximum element


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
        st.snow()
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
