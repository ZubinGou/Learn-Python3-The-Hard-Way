#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-23 16:06:14
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import tensorflow as tf
import numpy as np
import input_data
# from tensorflow.examples.tutorials.mnist import input_data


## 3 ways of load mnist

# # way 1
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# way 2
file = np.load("MNIST_data/mnist.npz")
x_train, y_train = file['x_train'], file['y_train']
x_test, y_test = file['x_test'], file['y_test']
file.close()

# # way 3
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# ??


x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test, verbose=2)
