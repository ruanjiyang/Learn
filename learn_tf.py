import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import matplotlib
# from keras.layers import Dense
# import matplotlib.pyplot as plt
# a=np.arange(10,dtype=int)
# a=np.random.rand(10).reshape(-1,1)
# print(a)
# print(a.shape)
# a=a.reshape(2,5)
# print(a.shape)
# print(a):w

# a=a.reshape(1,10)
# b=np.squeeze(a,axis=0)
# print(b.shape)
# print(b)
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a*b)
print(tf.keras.__version__)
print(tf.__version__)
model = Sequential()
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(optimizer=tf.keras.optimizers.SGD(0.001),
             loss=tf.keras.losses.categorical_crossentropy,
             metrics=[tf.keras.metrics.categorical_accuracy])


import numpy as np

train_x = np.random.random((1000, 1))
#train_y = np.random.random((1000, 10))
train_y=2*train_x+1

val_x = np.random.random((200, 1))
val_y = np.random.random((200, 10))

model.fit(train_x, train_y, epochs=10, batch_size=100,validation_data=(val_x, val_y))

print(model.summary())

print("train_x shape=",train_x.shape)