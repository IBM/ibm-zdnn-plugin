# Copyright 2022, 2023 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Sample Tensorflow application training with the Fashion MNIST data set.
Run this model with `fashion_mnist.py`.
"""
import os
import sys

import tensorflow as tf

def train():
    """
    Train a model for the Fashion MNIST dataset.
    """

    (X_train, y_train), (X_test, y_test) = \
        tf.keras.datasets.fashion_mnist.load_data()
    print(f'X_train shape:{X_train.shape}, y_train shape: {y_train.shape}')

    X_train = X_train.astype('float32') / 255
    X_test = X_test.astype('float32') / 255

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(
        64,
        7,
        padding='same',
        activation='relu',
        input_shape=[28, 28, 1]))
    model.add(tf.keras.layers.MaxPooling2D(2))
    model.add(tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'))
    model.add(tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(2))
    model.add(tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'))
    model.add(tf.keras.layers.Conv2D(256, 3, padding='same', activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(2))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    print(model.summary())

    model.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

    model.fit(X_train,
            y_train,
            batch_size=64,
            epochs=10,
            validation_data=(X_test, y_test))

    # Evaluate the model on test set
    score = model.evaluate(X_test, y_test, verbose=0)

    # Print test accuracy
    print('\n', 'Test accuracy:', score[1])
    model.save('./saved_model/1')


def has_nnpa():
    """
    Is ibm-zdnn-plugin enabled.
    """
    devs = tf.config.experimental.list_logical_devices(device_type='NNPA')
    return len(devs) > 0


if __name__ == '__main__':

    # Must be set before invoking any Tensorflow APIs
    os.environ['NNPA_DEVICES'] = '0'

    # Ensure ibm-zdnn-plugin is disabled for training.
    has_nnpa = has_nnpa()
    if has_nnpa:
        sys.exit('ibm-zdnn-plugin does not support training models.')
        

    try:
        # Train the model
        train()
    finally:
        # Enable ibm-zdnn-plugin for inference.
        print()
        if disable_nnpa:
            del os.environ['NNPA_DEVICES']
