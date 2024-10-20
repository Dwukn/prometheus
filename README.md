# Eye-Deep-Net

Eye-Deep-Net is a cutting-edge project aimed at leveraging Convolutional Neural Network (CNN) architectures to accurately predict retinal diseases from medical imaging data. This project focuses on enhancing early diagnosis and treatment strategies for conditions such as diabetic retinopathy, age-related macular degeneration, and glaucoma, making it a valuable tool for ophthalmologists and healthcare providers.

## Project Overview

In recent years, the importance of early detection of retinal diseases has become increasingly evident. Eye-Deep-Net utilizes deep learning techniques to analyze retinal images, improving diagnostic accuracy and helping to inform treatment decisions. The project includes:

- **Data Preprocessing**: Preparing medical imaging data to ensure optimal input for the models.
- **Model Training**: Implementing multiple CNN architectures, training them on a diverse dataset of retinal images.
- **Evaluation**: Assessing model performance to ensure high accuracy and reliability.

## Objectives

- Develop a robust model capable of classifying retinal diseases from medical images.
- Compare the effectiveness of different CNN architectures.
- Contribute to the field of medical imaging and machine learning through research.

## Features

- **Multiple CNN Models**: Includes several architectures for enhanced prediction capabilities.
- **High Accuracy**: Focus on achieving reliable predictions to aid in early diagnosis.
- **User-Friendly**: Designed for ease of use, making it accessible for healthcare professionals and researchers.

## Requirements

- Python 3.x
- TensorFlow / Keras
- NumPy
- Scikit-learn
- Pickle

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dwukn/EyeDeep-Net.git
   cd EyeDeep-Net
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

You can train the Eye-Deep-Net model using either the SGD or Adam optimizer. The model saves the best weights during training.

```python
# For SGD optimizer
opt = SGD(lr=0.001)
eyenet_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
```

### Model Evaluation

After training, the models can be evaluated on validation and test datasets. Validation accuracy will be displayed to indicate model performance.

```python
predict = eyenet_model.predict(X_val)
```

### Predicting with the Model

To make predictions on new images:

1. Ensure the trained model is saved in the `model/` directory (e.g., `extension_weights.hdf5`).
2. Use the provided `predict_retinal_disease.py` script. Update the `image_path` variable in the script with the path to your image.

Run the prediction script:

```bash
python predict_retinal_disease.py
```

This will display the input image along with the predicted retinal disease.



## Results

The project will output accuracy metrics for each model after validation and testing phases. Key metrics include:

- EyeNet SGD Validation Accuracy
- EyeNet Adam Validation Accuracy
- Extension Model Validation Accuracy

## Checkpoints and History

Model weights and training history are saved in the `model` directory for future reference:

- `model/sgd_weights.hdf5`: Weights for the EyeNet model trained with SGD.
- `model/adam_weights.hdf5`: Weights for the EyeNet model trained with Adam.
- `model/extension_weights.hdf5`: Weights for the extension model.
- `model/sgd_history.pckl`, `model/adam_history.pckl`, `model/extension_history.pckl`: Files containing training history.


## Acknowledgements

Thanks to the TensorFlow/Keras community for their invaluable resources that made this project possible.
