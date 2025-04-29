import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import os

# Define global variables
labels = []

# Load the model
model_path = "model/extension_weights.hdf5"  # Update this path if necessary
extension_model = load_model(model_path)

# Load class labels
path = "SelectedImages"  # Update this path if necessary
for root, dirs, directory in os.walk(path):
    for j in range(len(directory)):
        name = os.path.basename(root)
        if name not in labels:
            labels.append(name.strip())

def predict(image_path):
    # Load and preprocess the image
    image = cv2.imread(image_path)  # Read test image
    img = cv2.resize(image, (32, 32))  # Resize image to match model input size
    im2arr = np.array(img)
    im2arr = im2arr.reshape(1, 32, 32, 3)  # Convert image to 4D array
    img = np.asarray(im2arr).astype('float32')  # Convert to float
    img /= 255  # Normalize the image

    # Perform prediction
    predict = extension_model.predict(img)
    predicted_index = np.argmax(predict)  # Get the predicted class index

    # Display the image with the predicted label
    img = cv2.imread(image_path)
    img = cv2.resize(img, (400, 300))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.putText(img, 'Predicted As: ' + labels[predicted_index], (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    plt.figure(figsize=(4, 3))
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

if __name__ == "__main__":
    # Example usage
    image_path = "path/to/your/image.jpg"  # Update this with your image path
    predict(image_path)
