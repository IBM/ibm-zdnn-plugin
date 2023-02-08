# Fashion MNIST Sample

The code sample in this directory [loads](https://www.tensorflow.org/versions/r2.9/api_docs/python/tf/keras/datasets/fashion_mnist/load_data) the [Fashion MNIST data set](https://www.tensorflow.org/datasets/catalog/fashion_mnist) and trains a model. A second script performs inference on the model with the test data set and displays the results.

Some of the samples, or your own TensorFlow applications, will train models. IBM-zDNN-Plugin supports inferencing workloads only. Training workloads should be performed with a base Tensorflow build, or with IBM-zDNN-Plugin removed from the software installation or disabled as described in [Modifying Default Execution Paths](../../README.md#modifying-default-execution-paths).

The [samples README file](../README.md) contains general information on downloading and running the samples.

These samples will download the MNIST data set from the Internet.

## Running the Sample

Run these commands on and IBM Z System where you have installed Tensorflow and the ibm-zdnn-plugin pip package.

First, train and save the model to disk with the `fashion_mnist_training.py` script. This will download the fashion MNIST data set and create a model in the current directory.

Training will take some time. The epoch number in the output will indicate progress.

```bash
python fashion_mnist_training.py
```

Once the model has been trained, run the `fashion_mnist.py` script to run inference against the model.

```bash
python fashion_mnist.py
```

The script will report a prediction for some sample images.
