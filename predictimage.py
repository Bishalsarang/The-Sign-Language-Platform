import cv2
import argparse
import os
import numpy as np
from variables import *
from keras.models import load_model

model = load_model(MODEL_PATH)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the image")
args = vars(ap.parse_args())
IMG_PATH = args["image"]

if os.path.isfile(IMG_PATH):
    pass
else:
    print("File not found. Check the path")
    exit()


def preprocess_image(IMG_PATH):
    """
    :param IMG_PATH: path of the image
    :return: image array by preprocessing the image
    Example:
        img_array = preprocess_image("a.jpg")
    """
    # Load image with target size and convert img to array
    try:
        img = cv2.imread(IMG_PATH)
        # Change color sapce to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))

        # Reshape array to l * w * channels
        img_array = img.reshape(IMAGE_SIZE, IMAGE_SIZE, 1)
        # Normalize th array
        img_array = img_array / 225.0

        # Expand Dimension of the array as our model expects a 4D array
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print("Unexpected error", e)


def which_letter(IMG_PATH):
    """
    :param IMG_PATH: path of the image
    :return: confident_percent, predicted label using the model or None if exception occurs
    eg:
        print(which_letter("sample.jpeg"))
    """
    try:
        img_array = preprocess_image(IMG_PATH)
        preds = model.predict(img_array)
        preds *= 100
        most_likely_class_index = int(np.argmax(preds))
        return preds.max(), LABELS[most_likely_class_index]

    except Exception as e:
        print(e)
        return None


conf, label = which_letter(IMG_PATH)
print("The predicted letter is {} with {}%  confidence".format(label, conf))
