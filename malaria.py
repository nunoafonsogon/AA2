# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:09:43 2020

@author: Nuno
"""

################ IMPORTS
import numpy as np 
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt
import warnings
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten


import os
print(os.listdir(r"C:\Users\Nuno\Desktop\trabalhoAA2\input"))



################################ LER DADOS

parasitized = os.listdir(r"C:\Users\Nuno\Desktop\trabalhoAA2\input\cell_images\Parasitized")
uninfected = os.listdir(r"C:\Users\Nuno\Desktop\trabalhoAA2\input\cell_images\Uninfected")
parasitized.remove("Thumbs.db") #
uninfected.remove("Thumbs.db")  # 

tamanho=50 # Tamanho da imagem se tamanho =50 entao resize para 50X50

parasitized_images = []
for p in parasitized:
    img = Image.open(r"C:\Users\Nuno\Desktop\trabalhoAA2\input\cell_images\Parasitized\\"+p)
    img = img.resize((tamanho,tamanho))
    parasitized_images.append(img)

uninfected_images = []
for u in uninfected:
    img = Image.open(r"C:\Users\Nuno\Desktop\trabalhoAA2\input\cell_images\Uninfected\\"+u)
    img = img.resize((tamanho,tamanho))
    uninfected_images.append(img)
    

######################## PREPARAR DADOS


### juntar as duas pastas de imagens na variavel x
x_array = np.empty((len(parasitized_images)+len(uninfected_images), tamanho, tamanho, 3))
x_array = x_array.astype(int)
index = 0
for i in range(x_array.shape[0]):
    if i < len(parasitized_images):
        x_array[i] = np.array(parasitized_images[i])
    else:
        x_array[i] = np.array(uninfected_images[index])
        index += 1

# criar variavel y
y_array = np.append(np.ones(len(parasitized_images)), np.zeros(len(uninfected_images)))
y_array = to_categorical(y_array, num_classes = 2)


# dar split ao dataset para ter variaveis de treino e de teste
test_size=0.2
x_train, x_test, y_train, y_test = train_test_split(x_array, y_array, random_state = 42, test_size = test_size)
print("x_train shape: ",x_train.shape)
print("x_test shape: ",x_test.shape)
print("y_train shape: ",y_train.shape)
print("y_test shape: ",y_test.shape)
##################### Graficos bonitos

def print_history_accuracy(history):
    print(history.history.keys())
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

##################### MLP

def model_mlp(num_pixels):
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal',
                    activation='relu'))
    model.add(Dense(2, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def mlp(x_train,y_train,x_test,y_test):
    num_pixels=x_train.shape[1] * x_train.shape[2]*x_train.shape[3]
    print(x_train.shape)
    x_train = x_train.reshape(x_train.shape[0], num_pixels).astype('float32')
    x_test = x_test.reshape(x_test.shape[0], num_pixels).astype('float32')
    print(x_train.shape)

    x_train = x_train / 255
    x_test = x_test / 255

    model = model_mlp(num_pixels)
    print(model.summary())
    history=model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=3, batch_size=32,
                      verbose=2)
    print_history_accuracy(history)
    scores = model.evaluate(x_test, y_test, verbose=0)
    print('Scores: ', scores)
    print("Erro modelo MLP: %.2f%%" % (100-scores[1]*100))
    
    
mlp(x_train,y_train,x_test,y_test)
#################### CNN



