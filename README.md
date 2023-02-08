# IBM-zDNN-Plugin v1.1

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Model Validation](#model-validation)
4. [Execution on the Integrated Accelerator for AI and on CPU](#execution-on-the-integrated-accelerator-for-ai-and-on-cpu)
5. [Using the Code Samples](#using-the-code-samples)
6. [Frequently Asked Questions](#frequently-asked-questions)
7. [Working with us](#working-with-us)
8. [Licenses](#licensesnotices)
9. [Tested Linux® Distributions](#tested-linux-distributions)
10. [Disclaimer](#disclaimer)

## Overview

[TensorFlow](https://www.tensorflow.org/) is an open source machine learning framework. It has a comprehensive set of tools that enable model development, training, and inference. It also features a rich, robust ecosystem.

On IBM® z16™ hardware (running Linux on IBM Z or IBM® z/OS® Container Extensions (IBM zCX)), TensorFlow core 2.9 can leverage new inference acceleration capabilities by transparently targeting the IBM Integrated Accelerator for AI through the IBM-zDNN-Plugin. The IBM-zDNN-Plugin is a device plugin for TensorFlow ([PluggableDevice](https://blog.tensorflow.org/2021/06/pluggabledevice-device-plugins-for-TensorFlow.html)) that leverages the [IBM z Deep Neural Network](https://github.com/IBM/zDNN) (zDNN) library. The zDNN library contains a set of primitives that support Deep Neural Networks. These primitives transparently target the IBM Integrated Accelerator for AI on IBM z16™ hardware.

IBM-zDNN-Plugin supports inferencing workloads only. Training workloads should be performed with a base Tensorflow build, or with IBM-zDNN-Plugin removed from the software installation or disabled as described in [Modifying Default Execution Paths](#modifying-default-execution-paths).

## Getting Started

TensorFlow core 2.9 and zDNN >= 0.4.0 are prerequisites to successfully install the IBM-zDNN-Plugin.

### Installing TensorFlow core 2.9

- For Ubuntu 20.04 and Ubuntu 22.04, container images with pre-built and pre-installed TensorFlow core 2.9 have been made available on the [IBM Z and LinuxONE Container Registry](https://ibm.github.io/ibm-z-oss-hub/containers/tensorflow.html). To utilize the container images, you must gain access by following the instructions [here](https://ibm.github.io/ibm-z-oss-hub/main/main.html) in the section titled "Getting Started".

- Otherwise, please build and install TensorFlow from source by following the steps [here](https://github.com/linux-on-ibm-z/docs/wiki/Building-TensorFlow).

### Installing the zDNN >= 0.4.0

- For Ubuntu 22.04, you may install zDNN by using the package manager.
  - `apt-get update && apt-get install -y libzdnn-dev`
- Otherwise, please build and install zDNN from source by following the steps [here](https://github.com/IBM/zDNN).

After the above prerequisites have been successfully installed, (i.e., TensorFlow core 2.9 and zDNN >= 0.4.0 have successfully installed in your environment), you may proceed to installing the IBM-zDNN-Plugin.

### Installing IBM-zDNN-Plugin

- Install IBM-zDNN-Plugin from the binary distribution platform targetted for manylinux_2_27_s390x from [PyPi](https://pypi.org/project/ibm-zdnn-plugin/)
  - `pip3 install ibm-zdnn-plugin`
  - To verify that TensorFlow *will* leverage the ibm-zdnn-plugin to transparently target the IBM Integrated Accelerator for AI, issue the below commands. `NNPA` (Neural Network Processing Assist) will be listed as a PhysicalDevice.

    ```
      $ python
      >>> import tensorflow as tf
      >>> tf.config.list_physical_devices()
      [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:NNPA:0' device_type='NNPA')]
    ```

### Uninstalling IBM-zDNN-Plugin

- For any reason that you need to uninstall IBM-zDNN-Plugin
  - `pip3 uninstall ibm-zdnn-plugin`
  - To verify that TensorFlow will *not* leverage the ibm-zdnn-plugin to transparently target the IBM Integrated Accelerator for AI, issue the below commands. NNPA will not be listed as a PhysicalDevice.

    ```
    $ python
    >>> import tensorflow as tf
    >>> tf.config.list_physical_devices()
    [PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU')]
    ```

## Model Validation

The below list of models, but not limited to, trained on x86 or IBM Z, demonstrate focused optimizations that transparently target the IBM Integrated Accelerator for AI for a number of compute-intensive operations during inferencing.

- BERT
- Biomedical Image Segmentation
- Credit Card Fraud
- DenseNet121
- DenseNet169
- DenseNet201
- InceptionResNet
- InceptionV3
- NASNetLarge
- NMT
- ResNet101
- ResNet152
- ResNet50
- VGG16
- VGG19
- Xception
- YOLOV3
- YOLOv4

Many of these models can be found [here](https://www.tensorflow.org/versions/r2.9/api_docs/python/tf/keras/applications).

## Execution on the Integrated Accelerator for AI and on CPU

IBM-zDNN-Plugin follows IBM's train anywhere and deploy on IBM Z strategy.

### Default Execution Paths

When using the IBM-zDNN-Plugin on an IBM z16™ system, TensorFlow will transparently target the IBM Integrated Accelerator for AI for a number of compute-intensive operations during inferencing with no changes necessary to TensorFlow models.

### Modifying Default Execution Paths

To manually enforce which execution path should be followed, you may change the environment variable, NNPA_DEVICES, before execution starts.

- To transparently target the Integrated Accelerator for AI
  - `export NNPA_DEVICES=1` or `unset NNPA_DEVICES`
- To target the CPU only transparently
  - `export NNPA_DEVICES=0`

In application code, the environment variable should be set before the application calls any Tensorflow APIs.

## Using the Code Samples

Documentation for our code samples can be found [here](samples).

## Frequently Asked Questions

- Q: Where can I get the Base TensorFlow container image?
  - A: Please visit this link [here](https://ibm.github.io/ibm-z-oss-hub/containers/tensorflow.html).
- Where can I find steps to build TensorFlow on IBM z16™?
  - A: Please visit this link [here](https://ibm.github.io/ibm-z-oss-hub/containers/tensorflow.html).
- Q: How do I install the zDNN library?
  - A: As mentioned in the above section, “Getting Started”, on supported Linux distributions like Ubuntu 22.04, you may use a package manager to install. On other Linux distributions, it can be built and installed by source.

## Working with us

Want to report a bug, request a feature, or provide us feedback?
Contact us directly at [aionz@us.ibm.com](aionz@us.ibm.com) and become a member of the [AI on IBM Z Community](https://ibm.biz/aionibmz-community).

## Tested Linux Distributions

- Ubuntu 22.04
- Ubuntu 20.04
- Ubuntu 18.04 - Note. End of Support April 30, 2023
- Red Hat® Enterprise Linux® 8.7

## Logging Levels

To obtain logging/troubleshooting data about inferencing workloads, set the Tensorflow environment variables 'TF_CPP_MIN_LOG_LEVEL' and 'TF_CPP_MAX_VLOG_LEVEL'.

To enable the highest verbosity of logging, ensure the following environment variables are set as shown (examples show use the Bash shell):

```bash
export TF_CPP_MIN_LOG_LEVEL='0'
export TF_CPP_MAX_VLOG_LEVEL='4'
```

To return logging to the default, to show error and fatal messages:

```bash
export TF_CPP_MIN_LOG_LEVEL='2'
export TF_CPP_MAX_VLOG_LEVEL='0'

# Or remove the environment variables from the runtime environment.
unset TF_CPP_MIN_LOG_LEVEL
unset TF_CPP_MAX_VLOG_LEVEL
```

## Licenses/Notices

- The International License Agreement for Non-Warranted Programs (ILAN) agreement can be found [here](https://www14.software.ibm.com/cgi-bin/weblap/lap.pl?li_formnum=L-AJCQ-M4PQKX)
- The registered trademark Linux® is used pursuant to a sublicense from the Linux Foundation, the exclusive licensee of Linus Torvalds, owner of the mark on a worldwide basis.
- TensorFlow, the TensorFlow logo and any related marks are trademarks of Google Inc
- Ubuntu and Canonical are registered trademarks of Canonical Ltd.
- Red Hat and Red Hat Enterprise Linux are registered trademarks of Red Hat, Inc. in the United States and other countries.
- IBM, ibm.com, IBM Z, IBM z16,  LinuxONE, LinuxONE Emperor, LinuxONE Rockhopper, LinuxONE III, System z, z16, zEnterprise, z/OS, zSystems, Z Systems and z/VM are trademarks or registered trademarks of the International Business Machines Corporation.
- Additional license and notice files are within the `licenses-and-notices` directory of this repository. You may access the folder [here](licenses-and-notices).

## Disclaimer

IBM's statements regarding its plans, directions and intent are subject to change or withdrawal without notice at IBM's sole discretion. Information regarding potential future products is intended to outline our general product direction and it should not be relied on in making a purchasing decision. The information mentioned regarding potential future products is not a commitment, promise, or legal obligation to deliver any material, code or functionality. Information about potential future products may not be incorporated into any contract. The development, release, and timing of any future features or functionality described for our products remains at our sole discretion.
