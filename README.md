# Avacado Ripeness level classification using CNN:
This project predicts the ripeness level of avocados using deep learning. The model classifies avocado images into five ripeness stages, ranging from unripe to overripe, based on colour.

## Dataset: 
- The dataset is sourced from Mendeley Data, a cloud platform containing ~14000 avocado images captured at different ripening stages. 
- Each image is labeled with its corresponding ripeness level. 
- The dataset was organised in to 5 folders.

## Azure Blob storage:
- 5 folders were uploaded to Azure Blob Storage for safe, centralized, and remote access.
- The images were retrived into Numpy array (X and y), they make training process faster and memory efficient than uploading raw images every time.
- These arrays were saved back to Azure as X.npy and y.npy for direct loading in model training.

## EDA and Preprocessing:
- Data split : train(70), test(15) and validation(15)
- Each class dont have equal number of images so used class weights so that the model gives equal importance to all classes.
- Applied transformations like rotation, zoom, shift, and flip to make the model robust and prevent overfitting.
- Custom data generator: loaded data in batches instead of all at once.

## Model Architecture: 
- Built a CNN using tensorflow/keras.
- Used layers like Conv2D, BatchNormalization, MaxPooling2D, Dropout, GlobalAveragePooling2D, and Dense.
- Used EarlyStopping and ReduceLROnPlateau.

## Training and Performance: 
- used 30 epochs.
- Validation accuracy and test accuracy were noted.

Finally, a **Streamlit app** was deployed for easy use and visualization.
**Try the live app:** [Avocado Ripeness Level App](https://avacadoripenesslevel-sczeqpcsbruacdcy6exsju.streamlit.app/)
