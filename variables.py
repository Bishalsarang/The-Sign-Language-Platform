"""
Contains variables for image-size, path of models and labels that are required by other modules
"""
IMAGE_SIZE = 50  # We'll be working with 50 * 50 pixel images
MODEL_PATH = "trained_model\my_model.h5"

LABELS = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
LABELS.append("nothing")
LABELS.append("space")
