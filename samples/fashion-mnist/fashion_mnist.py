# Copyright 2022 IBM Corp.
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
Sample Tensorflow application with Fashion MNIST model trained by
`fashion_mnist_training.py`.
"""
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = \
    tf.keras.datasets.fashion_mnist.load_data()

X_test = X_test.astype('float32') / 255

model = tf.keras.models.load_model('./saved_model/1')
print(model.summary())

y_pred = model.predict(X_test, batch_size=64)

correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_test, tf.int64))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)
print('\n', 'Test accuracy:', accuracy.numpy())
