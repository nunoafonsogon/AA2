# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:09:43 2020

@author: Nuno
"""

################ IMPORTS
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras import backend as K
K.common.set_image_dim_ordering('th')


################ LOAD DATASET

def load_dataset(path):
    data = load_files(path)
    files = np.array(data['filenames'])
    targets = np.array(data['target'])
    target_labels = np.array(data['target_names'])
    return files,targets,target_labels
def convert_image_to_array(files):
    images_as_array=[]
    for file in files:
        # Convert to Numpy Array
        images_as_array.append(img_to_array(load_img(file)))
    return images_as_array

path=  r'C:\Users\Nuno\Desktop\cell_images'
x, y,target_labels = load_dataset(path)
x = np.array(convert_image_to_array(x))
print(x[1].shape)
num_pixels = x[1].shape[1] * x[1].shape[2] *x[1].shape[0]


x = x.astype('float32')
X = X / 255.0

print(x)
#X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=42)

################### 
###################
def print_history_accuracy(history):
    print(history.history.keys())
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
def create_compile_model_mlp(num_pixels, num_classes):
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal',
                    activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model




