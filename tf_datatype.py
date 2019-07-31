import tensorflow as tf
import numpy as np

tensor_0 = 1
tensor_1 = [b"Tensor", b"flow", b"is", b"great"]
tensor_2 = [[False, True, False], [True, True, False]]
tensor_3 = [[[0, 0, 0], [0, 0, 1]], [[1, 0, 0], [1, 0, 1]], [[2, 0, 0], [2, 0, 1]]]

print(type('Hello, Tensorflow!'))
print(type(tf.constant('Hello, Tensorflow!')))
print(type(tf.Session().run(tf.constant('Hello, Tensorflow!'))))

print(np.int8==tf.int8)
print(np.int16==tf.int16)
print(np.int64==tf.int64)


