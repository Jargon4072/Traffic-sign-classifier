# Traffic-sign-classifier
### Overview

### Dependencies
This project requires **Python 3.5** and the following Python libraries installed:
- [Jupyter](http://jupyter.org/)
- [NumPy](http://www.numpy.org/)
- [Scipy](https://www.scipy.org/)
- [Scitkit-learn](http://scikit-learn.org/)
- [TensorFlow](http://tensorflow.org)
- [Matplotlib](http://matplotlib.org/)
- [Pandas](http://pandas.pydata.org/)
- [OpenCV](http://opencv.org) useful for image processing.
- [This](https://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/) tutorial is very useful to install opencv. try this to install via conda `conda install -c https://conda.anaconda.org/menpo opencv3`.
- OpenCV can also be install with apt-get in Ubuntu.

### Dataset
- Dataset used is German Traffic Sign Recognition Bentchmark(GTSRB). [Download the dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset)  from here.
- The Training dataset contains 39,209 training images in 43 classes. The test dataset contains 12,630 test images.

### Model Architecture
The model is based on LeNet by Yann LeCun. It is a convolutional neural network designed to recognize visual patterns directly from pixel images with minimal preprocessing. It can handle hand-written characters very well too.