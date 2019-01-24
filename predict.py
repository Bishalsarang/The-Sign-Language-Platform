import cv2
import numpy as np
from variables import *
from keras.models import load_model


model = load_model(MODEL_PATH)

def pre_process(img_array):
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_array = cv2.resize(img_array, (50, 50))
    # Reshape array to l * w * channels
    img_array = img_array.reshape(IMAGE_SIZE, IMAGE_SIZE, 1)

    # Normalize th array
    img_array = img_array / 255.0

    # Expand Dimension of the array as our model expects a 4D array
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def which(img_array):
    img_array = pre_process(img_array)
    preds = model.predict(img_array)
    most_likely_class_index = int(np.argmax(preds))
    np.set_printoptions(suppress=True, precision=4)
    preds *= 100
    # print(preds)
    return preds.max(), LABELS[most_likely_class_index]


