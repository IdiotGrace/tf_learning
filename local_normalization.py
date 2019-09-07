#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 05:38:27 2017

@author: yhilly
"""

import tensorflow as tf
import numpy as np

input_data = np.array([i for i in range(0, 32)])
reshape_data = tf.reshape(input_data, [2, 2, 2, 4])
reshape_data2 = tf.to_float(reshape_data)

lrn = tf.nn.local_response_normalization(
    input = reshape_data2,
    depth_radius = 2,
    bias = 0,
    alpha = 1,
    beta = 1)

with tf.Session() as sess:
    print(reshape_data2.eval())
    print('----------------After LRN---------------------------')
    print(lrn.eval())
   