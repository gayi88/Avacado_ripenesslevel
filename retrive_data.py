import numpy as np
from azure.storage.blob import ContainerClient
from io import BytesIO
from PIL import Image
import os


container_sas_url = os.getenv("AZURE_CONTAINER_SAS_URL")
# Connect to Azure container
container_client = ContainerClient.from_container_url(container_sas_url)

print("📥 Retrieving images from Azure...")

X, y = [], []

# Looping through all blobs in container
for i, blob in enumerate(container_client.list_blobs()):
    if blob.name.endswith(".jpg") or blob.name.endswith(".png"):
        try:
            # Extract label from folder name (1, 2, 3, 4, 5)
            label = int(blob.name.split("/")[0])

            # Download image as stream
            blob_client = container_client.get_blob_client(blob)
            stream = BytesIO(blob_client.download_blob().readall())

            # Convert image to RGB and resize
            img = Image.open(stream).convert("RGB")
            img = img.resize((128, 128))

            # Convert to NumPy array
            img_array = np.array(img)
            X.append(img_array)
            y.append(label)

            # Print progress
            if (i + 1) % 50 == 0:
                print(f"{i + 1} images processed...")

        except Exception as e:
            print(f"⚠️ Skipping {blob.name}: {e}")

print("✅ All images retrieved and converted to NumPy arrays.")

# Convert to NumPy arrays
X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)
print("y shape:", y.shape)

# ✅ Upload X and y to Azure (not saving locally)
import io

print("☁️ Uploading X.npy and y.npy to Azure Blob Storage...")

# Convert arrays to bytes in memory
X_buffer = io.BytesIO()
np.save(X_buffer, X)
X_buffer.seek(0)

y_buffer = io.BytesIO()
np.save(y_buffer, y)
y_buffer.seek(0)

# Upload directly to Azure
X_blob = container_client.get_blob_client("X.npy")
y_blob = container_client.get_blob_client("y.npy")

X_blob.upload_blob(X_buffer, overwrite=True)
y_blob.upload_blob(y_buffer, overwrite=True)

print("✅ Uploaded X.npy and y.npy to Azure Blob Storage successfully.")
