#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-23 15:58:46
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import tensorflow as tf
import numpy as np
from tensorflow import keras


model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-2, 0, 1, 2, 3, 4], dtype=float)
ys = np.array([-2.3, 1.2, 3.4, 5.7, 10.2, 13.3], dtype=float)

model.fit(xs, ys,epochs=100)

print(model.predict([10.0]))
