import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


# Load Model

MODEL_PATH = "avocado_model.h5"

st.title("🥑 Avocado Ripeness Classifier")
st.write("Upload an image of an avocado to check its ripeness level.")

# Try loading model
try:
    model = load_model(MODEL_PATH)
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"⚠️ Error loading model:\n\n{e}")
    st.stop()

# Ripeness info
ripeness_info = {
    0: {"label": "Unripe", "message": "Need more than 1 week to ripen"},
    1: {"label": "Early Ripening", "message": "Can eat in 2-3 days"},
    2: {"label": "Perfect", "message": "Perfect for salad"},
    3: {"label": "Overripe", "message": "Perfect for making guacamole"},
    4: {"label": "Spoiled", "message": "Do not eat"},
}

# -----------------------
# File Upload
# -----------------------
uploaded_file = st.file_uploader("📸 Upload an avocado image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    img = image.load_img(uploaded_file, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])

    # Show ripeness level
    info = ripeness_info.get(predicted_class, {"label": "Unknown", "message": "No info available"})
    st.subheader(f"🥑 Ripeness Level: {info['label']}")

    # Show message in red
    st.markdown(f"<p style='color:red; font-size:20px'>{info['message']}</p>", unsafe_allow_html=True)

    # Show prediction probabilities
    st.write("🔢 Model prediction probabilities:")
    st.bar_chart(predictions[0])
