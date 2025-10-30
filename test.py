import os
from tensorflow.keras.models import load_model

MODEL_PATH = r"D:\EC_utbildning\avacado_ripeness_level\avocado_model.h5"

# 1️⃣ Check if the file exists
if os.path.exists(MODEL_PATH):
    print("✅ Model file found!")
else:
    print("❌ Model file NOT found at this path!")

# 2️⃣ Try loading the model
try:
    model = load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", e)
