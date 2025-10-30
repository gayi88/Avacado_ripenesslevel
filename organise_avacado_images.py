import os
import shutil
import pandas as pd

#path for images
imagespath = r"D:\EC_utbildning\avacado_ripeness_level\Avocado Ripening Dataset"
data_labels = r"D:\EC_utbildning\avacado_ripeness_level\Avocado Ripening Dataset.xlsx"

output_path = "dataset"

#create output folder
if not os.path.exists(output_path):
    os.makedirs(output_path)
    
#load excel file
df = pd.read_excel(data_labels)

#loop through each row 
for index, row in df.iterrows():
    img_name = str(row['File Name']).strip()

    # Add .jpg extension
    if not img_name.lower().endswith('.jpg'):
        img_name = img_name + '.jpg'
    
    ripeness_class = str(row['Ripening Index Classification']).strip()
    
    #create folder for class 
    class_folder = os.path.join(output_path, ripeness_class)
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)
    
    # source and destination paths
    src_path = os.path.join(imagespath, img_name)
    dst_path = os.path.join(class_folder, img_name)
    
    #copy image to the class folder
    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
    else:
        print(f"Image not found: {src_path}")
    
print("Images have been organized into class folders successfully!")
    
    
    


