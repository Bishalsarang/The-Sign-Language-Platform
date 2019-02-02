"""
Contains functions : pre_process() and which() that are needed by translator.py for predicting image from webcam
"""
import cv2
import numpy as np
from variables import *
from keras.models import load_model


# Loads pretrained CNN Model from MODEL_PATH
model = load_model(MODEL_PATH)


def pre_process(img_array):
    """
    :param img_array: image converted to np array
    :return:  img_array after pre-processing(converting to grayscale, resizing, normalizing) the  array
    """
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_array = cv2.resize(img_array, (50, 50))
    # Reshape array to l * w * channels
    img_array = img_array.reshape(IMAGE_SIZE, IMAGE_SIZE, 1)

    # Normalize the array
    img_array = img_array / 255.0

    # Expand Dimension of the array as our model expects a 4D array
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def which(img_array):
    """
    :param img_array: np array of image which is to be predicted
    :return: confidence precentage and predicted letter
    """
    img_array = pre_process(img_array)
    preds = model.predict(img_array)
    preds *= 100
    most_likely_class_index = int(np.argmax(preds))
    return preds.max(), LABELS[most_likely_class_index]
