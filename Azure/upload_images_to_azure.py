from azure.storage.blob import BlobServiceClient
import os


connection_string = "DefaultEndpointsProtocol=https;AccountName=avacadoimagesstorage;AccountKey=VigxdeaqLmrCXayQCgTFD0Lf7qEL2RVPRFwxSO6gy28u3SlZKXm153slxYmcobUs2YhCb87fdr84+AStjFMDeA==;EndpointSuffix=core.windows.net"
container_name = "avocado-images"
local_folder = r"D:\EC_utbildning\avacado_ripeness_level\dataset"


# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)


# Upload dataset folder with subfolders

print("Uploading dataset folder...")
total_files = 0

for root, dirs, files in os.walk(local_folder):
    for file in files:
        file_path = os.path.join(root, file)
        # Preserve subfolder structure (1,2,3,4,5)
        blob_path = os.path.relpath(file_path, local_folder)

        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_path, data=data, overwrite=True)

        total_files += 1
        if total_files % 100 == 0:
            print(f"✅ {total_files} files uploaded...")

print(f"🎉 Upload complete! {total_files} files uploaded successfully.")
