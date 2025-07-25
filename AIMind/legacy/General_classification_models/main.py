import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Import model builders
from neural_network import baseline_model, residual_model

# Paths
train_data_dir = '/path/to/train/dataset'
validation_data_dir = '/path/to/validation/dataset'

# Data generators
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

valid_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(101, 101),
    batch_size=32,
    class_mode='binary',
    shuffle=True)

validation_generator = valid_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(101, 101),
    batch_size=32,
    class_mode='binary',
    shuffle=False)

# Function to inspect dataset
def identify_dataset_size(generator):
    num_classes = generator.num_classes
    total_images = generator.samples
    image_shape = generator.image_shape

    class_counts = {}
    for class_name, class_index in generator.class_indices.items():
        class_count = len([f for f in generator.filenames if f.startswith(class_name + '/')])
        class_counts[class_name] = class_count

    return num_classes, total_images, image_shape, class_counts

# Inspect
num_classes_train, total_images_train, image_shape_train, class_counts_train = identify_dataset_size(train_generator)
num_classes_valid, total_images_valid, image_shape_valid, class_counts_valid = identify_dataset_size(validation_generator)

print("Training Dataset:")
print(f"Number of classes: {num_classes_train}")
print(f"Total images: {total_images_train}")
print(f"Image shape: {image_shape_train}")
print("Images per class:", class_counts_train)

print("\nValidation Dataset:")
print(f"Number of classes: {num_classes_valid}")
print(f"Total images: {total_images_valid}")
print(f"Image shape: {image_shape_valid}")
print("Images per class:", class_counts_valid)

# Build models
baseline = baseline_model()
residual = residual_model()

# Compile models
baseline.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
residual.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
baseline_history = baseline.fit(train_generator, validation_data=validation_generator, epochs=10)
residual_history = residual.fit(train_generator, validation_data=validation_generator, epochs=10)

# Predict probabilities
baseline_y_pred = baseline.predict(validation_generator, verbose=1)
residual_y_pred = residual.predict(validation_generator, verbose=1)

# Get true labels
true_labels = validation_generator.classes

# Compute ROC/AUC
baseline_fpr, baseline_tpr, _ = roc_curve(true_labels, baseline_y_pred)
baseline_auc = roc_auc_score(true_labels, baseline_y_pred)

residual_fpr, residual_tpr, _ = roc_curve(true_labels, residual_y_pred)
residual_auc = roc_auc_score(true_labels, residual_y_pred)

# Plot ROC
plt.figure(figsize=(8, 6))
plt.plot(baseline_fpr, baseline_tpr, label=f'Baseline (AUC = {baseline_auc:.2f})')
plt.plot(residual_fpr, residual_tpr, label=f'Residual (AUC = {residual_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Convert probs to binary class labels (threshold 0.5)
baseline_y_pred_classes = (baseline_y_pred > 0.5).astype(int)
residual_y_pred_classes = (residual_y_pred > 0.5).astype(int)

print("\nBaseline Model Classification Report:")
print(classification_report(true_labels, baseline_y_pred_classes))

print("\nResidual Model Classification Report:")
print(classification_report(true_labels, residual_y_pred_classes))
