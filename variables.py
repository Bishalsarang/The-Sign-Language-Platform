"""
Contains variables for image-size, path of models and labels that are required by other modules
"""
IMAGE_SIZE = 50  # We'll be working with 50 * 50 pixel images
MODEL_PATH = "trained_model/bglessmodelv1.h5"

LABELS = ['A', 'C', 'E', 'H', 'I', 'L', 'O', 'U', 'V', 'W']

# Minimum confidence percentage i.e allowed for prediction
THRESHOLD = 30
