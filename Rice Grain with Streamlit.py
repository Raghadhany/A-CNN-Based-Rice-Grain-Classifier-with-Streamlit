import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
model = load_model(r"C:\Users\maher\Desktop\rice_cnn_model.h5")
class_names = {
    0: "Arborio",
    1: "basmati",
    2: "Jasmine",
    3: "karacadag",
    4: "ipsala"
}

def preprocess_image(image):
    image = image.convert("L")
    image = image.resize((128, 128))
    img_array = np.array(image) / 255.0
    return np.expand_dims(img_array, axis=0)


st.title("📷 CNN Image Classifier")



uploaded_file = st.file_uploader("choose an image: ", type=["jpg", "png", "jpeg"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="downloaded image", use_column_width=True)

if st.button("classify 🔍"):
        with st.spinner("classifying..."):
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_index = int(np.argmax(prediction))
            predicted_class = class_names.get(predicted_index, "Unknown")

            st.success(f"✅ prediction: *{predicted_class}*")

