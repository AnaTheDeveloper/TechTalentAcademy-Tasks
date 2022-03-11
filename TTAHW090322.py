# Task 1
# Practical: Artificial Intelligence (AI)

# In Data Science we process a lot data through AI. With the General Data Protection Regulation (GDPR), it is becoming increasingly important to understand
# the ethics behind the data that is collected, stored, processed and evaluated.

# • Find out what Responsible AI is?
# • Find instances where AI has failed? Or been used maliciously or incorrectly.
# • Implications of when AI fails. There is a specific article in the GDPR Law that covers this, especially with
#   automated decision making. (opt in and out options).
# • What should organisations do to ensure that they are being responsible with AI and the wider use of data in general?
# • Maximum 500 words.

# ---------TO SEE THIS TASK PLEASE CLICK ON THE LINK BELOW---------------------------
# https://docs.google.com/document/d/1pf6u9zN_R1wQaGNSpiNWI2anSxnfEKVr/edit?usp=sharing&ouid=104314020022454311060&rtpof=true&sd=true

# IF LINK WAS UNSUCCESSFUL/DIDNT WORK PLEASE SEE GITHUB READ ME SECTION FOR WEEK 9!

# Extension Task 1

# Use the website to practice:https://machinelearningmastery.com/tensorflow-tut
# The steps and code are very similar – you should start to notice the similarities yourselves.
# This page features multiple neural network tutorials – if you chose to do this optional task, you only need
# to pick one of these.

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

if __name__ == '__main__':

    # Notes from website:

    # TensorFlow is the premier open-source deep learning framework developed and maintained by Google.
    #  tf.keras API beings the simplicity and ease of use of Keras to the TensorFlow project.
    # Using tf.keras allows you to design, fit, evaluate, and use deep learning models to make predictions in just a few
    # lines of code. It makes common deep learning tasks, such as classification and regression predictive modeling,
    # accessible to average developers looking to get things done.

    # After completing this tutorial, you will know:

    # The difference between Keras and tf.keras and how to install and confirm TensorFlow is working.
    # The 5-step life-cycle of tf.keras models and how to use the sequential and functional APIs.
    # How to develop MLP, CNN, and RNN models with tf.keras for regression, classification, and time series forecasting.
    # How to use the advanced features of the tf.keras API to inspect and diagnose your model.
    # How to improve the performance of your tf.keras model by reducing overfitting and accelerating training.

    # It is a large tutorial and as such, it is divided into five parts; they are:
    # 1. Install TensorFlow and tf.keras
        # What Are Keras and tf.keras?
        # How to Install TensorFlow
        # How to Confirm TensorFlow Is Installed
    # 2. Deep Learning Model Life-Cycle
        # The 5-Step Model Life-Cycle
        # Sequential Model API (Simple)
        # Functional Model API (Advanced)
    # 3. How to Develop Deep Learning Models
        # Develop Multilayer Perceptron Models
        # Develop Convolutional Neural Network Models
        # Develop Recurrent Neural Network Models
    # 4. How to Use Advanced Model Features
        # How to Visualize a Deep Learning Model
        # How to Plot Model Learning Curves
        # How to Save and Load Your Model
    # 5. How to Get Better Model Performance
        # How to Reduce Overfitting With Dropout
        # How to Accelerate Training With Batch Normalization
        # How to Halt Training at the Right Time With Early Stopping

    # Keras is an open-source deep learning library written in Python.
    # The project was started in 2015 by Francois Chollet. It quickly became a popular framework for developers.
    # A secondary reason Keras took-off was because it allowed you to use any one among the range of popular deep learning
    # mathematical libraries as the backend (e.g. used to perform the computation), such as TensorFlow, Theano, and
    # later, CNTK. This allowed the power of these libraries to be harnessed (e.g. GPUs) with a very clean and simple interface.

    # In 2019, Google released a new version of their TensorFlow deep learning library (TensorFlow 2) that integrated the
    # Keras API directly and promoted this interface as the default or standard interface for deep learning development on
    # the platform.
    # This integration is commonly referred to as the tf.keras interface or API (“tf” is short for “TensorFlow“). This is
    # to distinguish it from the so-called standalone Keras open source project.
    # Standalone Keras. The standalone open source project that supports TensorFlow, Theano and CNTK backends.
    # tf.keras. The Keras API integrated into TensorFlow 2.

    # The 5-Step Model Life-Cycle
    # A model has a life-cycle, and this very simple knowledge provides the backbone for both modeling a dataset and understanding the tf.keras API.
    # The five steps in the life-cycle are as follows:
    # 1. Define the model.
    # 2. Compile the model.
    # 3. Fit the model.
    # 4. Evaluate the model.
    # 5. Make predictions.

    # 1. Defining the layers of the model, configuring each layer with a number of nodes and activation function,
    # and connecting the layers together into a cohesive model.

    # 2. Compiling the model requires that you first select a loss function that you want to optimize, such as mean squared error or cross-entropy.
    # It also requires that you select an algorithm to perform the optimization procedure, typically stochastic gradient descent,
    # or a modern variation, such as Adam. It may also require that you select any performance metrics to keep track of during the model training process.

    # The three most common loss functions are:
    # ‘binary_crossentropy‘ for binary classification.
    # ‘sparse_categorical_crossentropy‘ for multi-class classification.
    # ‘mse‘ (mean squared error) for regression.

    # 3. Fitting the model requires that you first select the training configuration, such as the number of epochs (loops through the
    # training dataset) and the batch size (number of samples in an epoch used to estimate model error). Training applies the chosen
    # optimization algorithm to minimize the chosen loss function and updates the model using the backpropagation of error algorithm.

    # 4. Evaluating the model requires that you first choose a holdout dataset used to evaluate the model. This should be
    # data not used in the training process so that we can get an unbiased estimate of the performance of the model when making
    # predictions on new data. The speed of model evaluation is proportional to the amount of data you want to use for the
    # evaluation, although it is much faster than training as the model is not changed.

    # 5. It requires you have new data for which a prediction is required, e.g. where you do not have the target values.
    # You may want to save the model and later load it to make predictions. You may also choose to fit a model on all of the
    # available data before you start using it.

    # Sequential Model API

    # The example below defines a Sequential MLP model that accepts eight inputs, has one hidden layer with 10 nodes and then an output layer with one node to predict a numerical value.

    # Multilayer Perception Model for Binary Classification

    # load the dataset
    path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/ionosphere.csv'
    df = read_csv(path, header=None)

    # split into input and output columns
    X, y = df.values[:, :-1], df.values[:, -1]

    # ensure all data are floating point values
    X = X.astype('float32')

    # encode strings to integer
    y = LabelEncoder().fit_transform(y)

    # split into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # determine the number of input features
    n_features = X_train.shape[1]

    # define model
    model = Sequential()
    model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
    model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
    model.add(Dense(1, activation='sigmoid'))

    # compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # fit the model
    model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=0)

    # evaluate the model
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print('Test Accuracy: %.3f' % acc)

    # make a prediction
    row = [1, 0, 0.99539, -0.05889, 0.85243, 0.02306, 0.83398, -0.37708, 1, 0.03760, 0.85243, -0.17755, 0.59755, -0.44945,
           0.60536, -0.38223, 0.84356, -0.38542, 0.58212, -0.32192, 0.56971, -0.29674, 0.36946, -0.47357, 0.56811, -0.51171,
           0.41078, -0.46168, 0.21266, -0.34090, 0.42267, -0.54487, 0.18641, -0.45300]
    yhat = model.predict([row])

    print('Predicted: %.3f' % yhat)
