# Lesson Objectives:
# What is Tensorflow.
# History of TensorFlow
# Deep Learning
# Artificial Neutral Networks

# What is Tensor Flow?
# TensorFlow is a Python-friendly open-source library for numerical computation that makes machine learning faster
# and easier.
# It is designed to enable fast experimentation with the deep Neural Network.
# TensorFlow is user-friendly, making it easy to create machine learning models.
# High and low-level neural network API.
# It can be used to train & serve models in live mode to real customers. Therefore, industrial researchers
# can apply their ideas to products faster.
# TensorFlow allows you to make the most of your available hardware with its advanced support

# History of TensorFlow?
# TensorFlow was released in 2015 and was developed by The Google Brains Team. It came off the back of the
# DistBelief machine learning system that was built in 2011.
# TensorFlow has a flexible architecture allowing for easy implementation of computation
# across a variety of platforms.

# What is deep learning?
# Machine learning, is the study of computer algorithms that improve automatically through experience.
# Deep learning is part of a broader family of machine learning methods based on artificial neural networks with
# representation learning.
# Artificial neural networks (ANNs) were inspired by information processing and distributed communication
# nodes in biological systems (brain).
# Deep learning is one of the hottest fields in data science with many case studies that have astonishing results in
# robotics, image recognition and Artificial Intelligence (AI).

# Artificial Neural Networks
# A neural network is created by connecting neurons. The human brain is then an example of such a neural network,
# which is composed of billions of neurons.
# The brain is proficient in performing quite complex calculations, and this is where the inspiration for Artificial
# Neural Networks comes from.
# The network on a whole is a powerful modelling tool.

# The Steps for Machine Learning:
# • Load dataset
# • Explore dataset
# • Process data
# • Visualise data
# • Pick algorithms
# • Train and test sets
# • Standardise data (scale)
# • Compile and fit
# • Learning from the model and evaluations

#------------------------------------Predicting Red or White Wine-----------------------------------------------------#
# Goals:
# 1. Get started with TensorFlow.
# 2. Familiarize yourself with how neural networks work.
# 3. Load the dataset and make sure you understand it. ie Acids, Sugar Sulphates, Wine Quality etc

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score

if __name__ == '__main__':

    # ---------Loading the dataset-------------
    # Import Dataset of white wine.
    white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
                        sep=";")

    # Import dataset of red wine.
    red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
                      sep=";")

    # ---------Exploring the dataset-------------
    # Exploring the white wine dataset
    print("The top 5 Results from the imported dataset of white wine: \n", white.head())
    print("The bottom 5 results from the dataset of white wine: \n", white.tail())
    # Pandas dataframe.info() function is used to get a concise summary of the dataframe.
    # The dataframe.describe() method computes and displays summary statistics for a Python dataframe.
    print("A quick summary of the white wine dataset: \n", white.info())
    print("A quick summary of the white wines data statistics: \n", white.describe())
    print("Checking for any null values within the white wine dataset: \n", pd.isnull(white))

    # Exploring the red wine dataset
    print("The top 5 Results from the imported dataset of red wine: \n", red.head())
    print("The bottom 5 results from the dataset of red wine: \n", red.tail())
    print("A quick summary of the red wine dataset: \n", red.info())
    print("A quick summary of the red wines data statistics: \n", red.describe())
    print("Checking for any null values within the red wine dataset: \n", pd.isnull(red))

    # ---------Visualise data--------------------
    # Bar chart for the distribution of alcohol in % vol.
    fig, ax = plt.subplots(1, 2)

    ax[0].hist(red.alcohol, 10, facecolor='red',
               alpha=0.5, ec='black',
               label='Red Wine')
    ax[1].hist(white.alcohol, 10, facecolor='white',
               alpha=0.5, ec='black',
               lw=0.5, label='White Wine')

    ax[0].set_xlabel("Alcohol in % Vol")
    ax[0].set_ylabel("Frequency")

    ax[1].set_xlabel("Alcohol in % Vol")
    ax[1].set_ylabel("Frequency")

    fig.subplots_adjust(wspace=0.5)
    fig.suptitle("Distribution of Alcohol in % Vol")

    plt.show()

    # A scatter bar chart showing the wine quality by amount of sulphates.
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))

    ax[0].scatter(red['quality'], red['sulphates'],
                  color='red')
    ax[1].scatter(white['quality'], white['sulphates'],
                  color='white', edgecolors='black',
                  lw=0.5)

    ax[0].set_title("Red Wine")
    ax[0].set_xlabel("Quality")
    ax[0].set_ylabel("Sulphates")

    ax[1].set_title("White Wine")
    ax[1].set_xlabel("Quality")
    ax[1].set_ylabel("Sulphates")

    fig.subplots_adjust(wspace=0.5)
    fig.suptitle("Wine Quality by Amount of Sulphates")

    plt.show()

    # Exploratory Data Analysis
    # Recap of what has been seen during your EDA that could be important :
    # • Some of the variables of your data sets have values that are significantly far apart.
    # • You have an ideal scenario: there are no null values in the data sets.
    # • Most wines included in the data set have around 9% of alcohol.
    # • Red wine seems to contain more sulphates than the white wine, which has less sulphates above 1 g/dm3

     # -------Processing the dataset-------------
    # Changing the type of the datasets from a string value to an integer. This is so we can use the type as a label.
    white['type'] = 0   # Add 'type' column to 'white' with value of 0
    red['type'] = 1     # Add 'type' column to 'red' with value of 1
    print("Changed type of dataset from a string to an int: \n", white.head())

    # Connect/Appending the two datasets to be one, to feed into the Artificial Neural Network.
    wines = red.append(white, ignore_index=True)
    # FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
    print("This is the two datasets of red and white wine connected and fed into the ANN: \n", wines)

    # Creating values for the data (X) and labels y.
    X = wines
    y = np.ravel(wines.type)

    # Dropping/removing the targets from the dataframe.
    X = X.drop(columns=['type'])


    # ---------Pick algorithms-------------------



    # ---------Train and test sets---------------
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print("The x_train shape is: \n", X_train.shape)
    print("The x_test shape is: \n", X_test.shape)

    # ---------Standardise data (scale)----------
    # Standardisation is a way to deal with the values that lie so far apart.
    # The scikit-learn package offers you a great and fast way of getting your data standardised:
    # Import the Standard Scaler module from sklearn.preprocessing and you’re ready to scale your train and test data!

    scalar = StandardScaler().fit(X_train)
    X_train = scalar.transform(X_train)
    X_test = scalar.transform(X_test)

    # ---------------Creating an ANN----------------
    # Creating the model
    model = Sequential()

    # Creating the model's layers:
    # A quick way to start building your multi-layer perceptron is to use the Keras Sequential model.
    # This is a linear stack of layers. You can easily create the model by passing a list of layer instances to the
    # constructor, you set this up by running: model = Sequential().

    # Input layer
    model.add(Dense(12, activation='relu', input_shape=(12,)))
    # Hidden layer
    model.add(Dense(8, activation='relu'))
    # Output label
    model.add(Dense(1, activation='sigmoid'))

    # Exploring the models parameters:
    print("Output shape: \n", model.output_shape)
    print("Model weights: \n", model.get_weights())

    # ---------Compile and fit-------------------
    # Compile the model.
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Fit the model.
    model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1)

    # ---------Learning from the model and evaluations-------------
    # Predict with the model.
    # Now we can use this data to predict which is a red/white wine?
    # 1 means it is likely to be a red wine and 0 it is likely to be a white wine!

    y_pred = model.predict(X_test)
    print("Predictions 1: \n", y_pred[:15])

    predictions = [1 if p > 0.5 else 0 for p in y_pred]

    print("Predictions 2: \n", predictions[:15])

    print("Predictions 3: \n",y_test[:15])

    # Evaluating the model.
    # This is using the model just built using the test data to make a prediction using data the model hasn’t used.
    # This evaluates the performance of the model, eg: how good the model is.
    score = model.evaluate(X_test, y_test, verbose=1)
    print("The model score: \n", score)

    # Before you start re-arranging the data and putting it together in a different way, it’s always a good idea to
    # try out different evaluation metrics.
    # For this, you can rely on scikit-learn (>> import as sklearn) for this. You will test out some basic
    # classification evaluation techniques like:
    # • The confusion matrix – This is a breakdown of predictions into a table showing correct predictions
    #   and the types of incorrect predictions that have been made.
    # • You should only see numbers in the diagonal, which means that all your predictions were correct!
    # • Precision is a measure of a classifier’s exactness. The higher the precision, the more accurate the classifier.

    confusion_matrix(y_test, predictions)
    precision_score(y_test, y_pred.round())

    # ---------------------------------------------------TERMINAL OUTPUT----------------------------------------------#

    # The top 5 Results from the imported dataset of white wine:
    #     fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 0            7.0              0.27         0.36  ...       0.45      8.8        6
    # 1            6.3              0.30         0.34  ...       0.49      9.5        6
    # 2            8.1              0.28         0.40  ...       0.44     10.1        6
    # 3            7.2              0.23         0.32  ...       0.40      9.9        6
    # 4            7.2              0.23         0.32  ...       0.40      9.9        6
    # [5 rows x 12 columns]
    # The bottom 5 results from the dataset of white wine:
    #        fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 4893            6.2              0.21         0.29  ...       0.50     11.2        6
    # 4894            6.6              0.32         0.36  ...       0.46      9.6        5
    # 4895            6.5              0.24         0.19  ...       0.46      9.4        6
    # 4896            5.5              0.29         0.30  ...       0.38     12.8        7
    # 4897            6.0              0.21         0.38  ...       0.32     11.8        6
    # [5 rows x 12 columns]
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 4898 entries, 0 to 4897
    # Data columns (total 12 columns):
    #  #   Column                Non-Null Count  Dtype
    # ---  ------                --------------  -----
    #  0   fixed acidity         4898 non-null   float64
    #  1   volatile acidity      4898 non-null   float64
    #  2   citric acid           4898 non-null   float64
    #  3   residual sugar        4898 non-null   float64
    #  4   chlorides             4898 non-null   float64
    #  5   free sulfur dioxide   4898 non-null   float64
    #  6   total sulfur dioxide  4898 non-null   float64
    #  7   density               4898 non-null   float64
    #  8   pH                    4898 non-null   float64
    #  9   sulphates             4898 non-null   float64
    #  10  alcohol               4898 non-null   float64
    #  11  quality               4898 non-null   int64
    # dtypes: float64(11), int64(1)
    # memory usage: 459.3 KB
    # A quick summary of the white wine dataset:
    #  None
    # A quick summary of the white wines data statistics:
    #         fixed acidity  volatile acidity  ...      alcohol      quality
    # count    4898.000000       4898.000000  ...  4898.000000  4898.000000
    # mean        6.854788          0.278241  ...    10.514267     5.877909
    # std         0.843868          0.100795  ...     1.230621     0.885639
    # min         3.800000          0.080000  ...     8.000000     3.000000
    # 25%         6.300000          0.210000  ...     9.500000     5.000000
    # 50%         6.800000          0.260000  ...    10.400000     6.000000
    # 75%         7.300000          0.320000  ...    11.400000     6.000000
    # max        14.200000          1.100000  ...    14.200000     9.000000
    # [8 rows x 12 columns]
    # Checking for any null values within the white wine dataset:
    #        fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 0             False             False        False  ...      False    False    False
    # 1             False             False        False  ...      False    False    False
    # 2             False             False        False  ...      False    False    False
    # 3             False             False        False  ...      False    False    False
    # 4             False             False        False  ...      False    False    False
    #              ...               ...          ...  ...        ...      ...      ...
    # 4893          False             False        False  ...      False    False    False
    # 4894          False             False        False  ...      False    False    False
    # 4895          False             False        False  ...      False    False    False
    # 4896          False             False        False  ...      False    False    False
    # 4897          False             False        False  ...      False    False    False
    # [4898 rows x 12 columns]
    # The top 5 Results from the imported dataset of red wine:
    #     fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 0            7.4              0.70         0.00  ...       0.56      9.4        5
    # 1            7.8              0.88         0.00  ...       0.68      9.8        5
    # 2            7.8              0.76         0.04  ...       0.65      9.8        5
    # 3           11.2              0.28         0.56  ...       0.58      9.8        6
    # 4            7.4              0.70         0.00  ...       0.56      9.4        5
    # [5 rows x 12 columns]
    # The bottom 5 results from the dataset of red wine:
    #        fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 1594            6.2             0.600         0.08  ...       0.58     10.5        5
    # 1595            5.9             0.550         0.10  ...       0.76     11.2        6
    # 1596            6.3             0.510         0.13  ...       0.75     11.0        6
    # 1597            5.9             0.645         0.12  ...       0.71     10.2        5
    # 1598            6.0             0.310         0.47  ...       0.66     11.0        6
    # [5 rows x 12 columns]
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 1599 entries, 0 to 1598
    # Data columns (total 12 columns):
    #  #   Column                Non-Null Count  Dtype
    # ---  ------                --------------  -----
    #  0   fixed acidity         1599 non-null   float64
    #  1   volatile acidity      1599 non-null   float64
    #  2   citric acid           1599 non-null   float64
    #  3   residual sugar        1599 non-null   float64
    #  4   chlorides             1599 non-null   float64
    #  5   free sulfur dioxide   1599 non-null   float64
    #  6   total sulfur dioxide  1599 non-null   float64
    #  7   density               1599 non-null   float64
    #  8   pH                    1599 non-null   float64
    #  9   sulphates             1599 non-null   float64
    #  10  alcohol               1599 non-null   float64
    #  11  quality               1599 non-null   int64
    # dtypes: float64(11), int64(1)
    # memory usage: 150.0 KB
    # A quick summary of the red wine dataset:
    #  None
    # A quick summary of the red wines data statistics:
    #         fixed acidity  volatile acidity  ...      alcohol      quality
    # count    1599.000000       1599.000000  ...  1599.000000  1599.000000
    # mean        8.319637          0.527821  ...    10.422983     5.636023
    # std         1.741096          0.179060  ...     1.065668     0.807569
    # min         4.600000          0.120000  ...     8.400000     3.000000
    # 25%         7.100000          0.390000  ...     9.500000     5.000000
    # 50%         7.900000          0.520000  ...    10.200000     6.000000
    # 75%         9.200000          0.640000  ...    11.100000     6.000000
    # max        15.900000          1.580000  ...    14.900000     8.000000
    # [8 rows x 12 columns]
    # Checking for any null values within the red wine dataset:
    #        fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
    # 0             False             False        False  ...      False    False    False
    # 1             False             False        False  ...      False    False    False
    # 2             False             False        False  ...      False    False    False
    # 3             False             False        False  ...      False    False    False
    # 4             False             False        False  ...      False    False    False
    #              ...               ...          ...  ...        ...      ...      ...
    # 1594          False             False        False  ...      False    False    False
    # 1595          False             False        False  ...      False    False    False
    # 1596          False             False        False  ...      False    False    False
    # 1597          False             False        False  ...      False    False    False
    # 1598          False             False        False  ...      False    False    False
    # [1599 rows x 12 columns]
    # Changed type of dataset from a string to an int:
    #     fixed acidity  volatile acidity  citric acid  ...  alcohol  quality  type
    # 0            7.0              0.27         0.36  ...      8.8        6     0
    # 1            6.3              0.30         0.34  ...      9.5        6     0
    # 2            8.1              0.28         0.40  ...     10.1        6     0
    # 3            7.2              0.23         0.32  ...      9.9        6     0
    # 4            7.2              0.23         0.32  ...      9.9        6     0
    # [5 rows x 13 columns]
    # This is the two datasets of red and white wine connected and fed into the ANN:
    #        fixed acidity  volatile acidity  citric acid  ...  alcohol  quality  type
    # 0               7.4              0.70         0.00  ...      9.4        5     1
    # 1               7.8              0.88         0.00  ...      9.8        5     1
    # 2               7.8              0.76         0.04  ...      9.8        5     1
    # 3              11.2              0.28         0.56  ...      9.8        6     1
    # 4               7.4              0.70         0.00  ...      9.4        5     1
    #              ...               ...          ...  ...      ...      ...   ...
    # 6492            6.2              0.21         0.29  ...     11.2        6     0
    # 6493            6.6              0.32         0.36  ...      9.6        5     0
    # 6494            6.5              0.24         0.19  ...      9.4        6     0
    # 6495            5.5              0.29         0.30  ...     12.8        7     0
    # 6496            6.0              0.21         0.38  ...     11.8        6     0
    # [6497 rows x 13 columns]
    # The x_train shape is:
    #  (4352, 12)
    # The x_test shape is:
    #  (2145, 12)
    # Output shape:
    #  (None, 1)
    # Model weights:
    #  [array([[ 0.37032282,  0.05305362,  0.25336766,  0.07338214,  0.01281869,
    #         -0.41383898,  0.27934968,  0.15590096,  0.01982152, -0.21652925,
    #         -0.14831066,  0.36294675],
    #        [ 0.27809   , -0.42893708,  0.30038893,  0.06546569,  0.15218127,
    #         -0.47655642, -0.27149582, -0.2415334 ,  0.02162468,  0.09406841,
    #          0.23992205,  0.39500046],
    #        [-0.22623754, -0.47486627,  0.24521518,  0.2504704 ,  0.42706823,
    #         -0.4441657 ,  0.25177276, -0.18314195,  0.08685374, -0.2057395 ,
    #         -0.12996602,  0.0731746 ],
    #        [-0.12412119, -0.3909632 ,  0.49538994, -0.06913781,  0.29028046,
    #         -0.2680658 ,  0.42217743,  0.2446593 , -0.34365916,  0.21627069,
    #          0.4387715 , -0.22619343],
    #        [ 0.08084691, -0.01769865, -0.09345567, -0.00118017, -0.03958488,
    #         -0.2868352 ,  0.451643  , -0.11985493, -0.44720423, -0.33134878,
    #         -0.07660854,  0.37230122],
    #        [-0.25845695, -0.10918796,  0.319736  ,  0.39371347,  0.25265443,
    #         -0.3953445 , -0.37228465, -0.0657407 ,  0.20754576,  0.03252339,
    #          0.39398682,  0.37373984],
    #        [ 0.33007383, -0.28327417, -0.21791065,  0.4228176 ,  0.15198219,
    #          0.3905971 ,  0.02937686,  0.42267764,  0.45803392,  0.09053385,
    #         -0.04765964,  0.4243412 ],
    #        [-0.11171448,  0.40887547, -0.13834453,  0.09325814,  0.23913872,
    #         -0.26408303, -0.22999275, -0.17520392, -0.2855215 ,  0.47832918,
    #          0.22059989, -0.1559521 ],
    #        [ 0.48573065,  0.05622602, -0.34641564, -0.45369983,  0.44839847,
    #         -0.08001614, -0.3929739 ,  0.19664812,  0.33066416,  0.1419549 ,
    #          0.30520594, -0.48261964],
    #        [ 0.26038897,  0.09081376, -0.3322296 , -0.06126332,  0.4426663 ,
    #         -0.03593719,  0.10009074,  0.34495866, -0.33107173,  0.39731097,
    #          0.45176256,  0.36298418],
    #        [-0.07060707, -0.12204707,  0.3003627 ,  0.30741823, -0.44470954,
    #          0.15065312,  0.23068643, -0.12425196,  0.37860632,  0.27214968,
    #          0.07293653,  0.05211711],
    #        [-0.4505576 , -0.16171992,  0.00074708, -0.26958585, -0.1629734 ,
    #          0.2728542 ,  0.33755887,  0.43758857, -0.40470302, -0.27037477,
    #         -0.43153107, -0.05195427]], dtype=float32), array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), array([[-0.29960513, -0.16396728,  0.08881837,  0.31859815, -0.43805176,
    #          0.2935331 ,  0.4190781 ,  0.13476813],
    #        [-0.42160898,  0.23388565, -0.20015967,  0.28429675,  0.0150882 ,
    #         -0.25665525,  0.4291187 ,  0.4349755 ],
    #        [-0.04134732,  0.08617073, -0.48308855,  0.28818738, -0.39335895,
    #          0.21531653, -0.43948418,  0.16776764],
    #        [-0.2319018 , -0.46270466,  0.10137957,  0.22963947, -0.00260049,
    #          0.376796  , -0.5383861 ,  0.13177872],
    #        [ 0.19514185,  0.08475828, -0.53991723,  0.25229025, -0.23013037,
    #          0.19638884,  0.13456714,  0.2281251 ],
    #        [ 0.241413  ,  0.42675465, -0.2661073 , -0.36680624, -0.5305385 ,
    #          0.29666728, -0.10049653,  0.19422698],
    #        [ 0.14651078,  0.08683503,  0.3710096 , -0.26376364,  0.07215571,
    #          0.02447295,  0.02069587,  0.04348332],
    #        [-0.36113614, -0.06022424, -0.16190323,  0.5302273 , -0.1521259 ,
    #          0.12457889,  0.25874543,  0.53936434],
    #        [-0.26385686,  0.10004538, -0.27916652, -0.12323165, -0.26785493,
    #          0.28621656,  0.22999454,  0.1948837 ],
    #        [-0.50113547, -0.48903367,  0.17494667,  0.22915488,  0.44395363,
    #          0.47976482,  0.12119395, -0.5292344 ],
    #        [-0.21321788,  0.2730947 , -0.16118056, -0.498177  ,  0.5260408 ,
    #         -0.5188482 , -0.3756057 , -0.3138501 ],
    #        [-0.42276835,  0.28639466, -0.36138606,  0.49517703, -0.5017958 ,
    #         -0.2889223 ,  0.32659608,  0.46695626]], dtype=float32), array([0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32), array([[-0.024095  ],
    #        [-0.5756069 ],
    #        [ 0.70944595],
    #        [ 0.3047601 ],
    #        [-0.04446119],
    #        [-0.14383197],
    #        [ 0.49320388],
    #        [-0.34019297]], dtype=float32), array([0.], dtype=float32)]
    # Epoch 1/20
    # 4352/4352 [==============================] - 3s 657us/step - loss: 0.0641 - accuracy: 0.9876
    # Epoch 2/20
    # 4352/4352 [==============================] - 3s 663us/step - loss: 0.0251 - accuracy: 0.9952
    # Epoch 3/20
    # 4352/4352 [==============================] - 3s 671us/step - loss: 0.0225 - accuracy: 0.9961
    # Epoch 4/20
    # 4352/4352 [==============================] - 3s 700us/step - loss: 0.0191 - accuracy: 0.9959
    # Epoch 5/20
    # 4352/4352 [==============================] - 3s 661us/step - loss: 0.0188 - accuracy: 0.9966
    # Epoch 6/20
    # 4352/4352 [==============================] - 3s 678us/step - loss: 0.0167 - accuracy: 0.9972
    # Epoch 7/20
    # 4352/4352 [==============================] - 3s 647us/step - loss: 0.0159 - accuracy: 0.9970
    # Epoch 8/20
    # 4352/4352 [==============================] - 3s 652us/step - loss: 0.0146 - accuracy: 0.9968
    # Epoch 9/20
    # 4352/4352 [==============================] - 3s 646us/step - loss: 0.0140 - accuracy: 0.9970
    # Epoch 10/20
    # 4352/4352 [==============================] - 3s 641us/step - loss: 0.0133 - accuracy: 0.9975
    # Epoch 11/20
    # 4352/4352 [==============================] - 3s 647us/step - loss: 0.0127 - accuracy: 0.9972
    # Epoch 12/20
    # 4352/4352 [==============================] - 3s 655us/step - loss: 0.0122 - accuracy: 0.9975
    # Epoch 13/20
    # 4352/4352 [==============================] - 3s 643us/step - loss: 0.0116 - accuracy: 0.9979
    # Epoch 14/20
    # 4352/4352 [==============================] - 3s 634us/step - loss: 0.0118 - accuracy: 0.9970
    # Epoch 15/20
    # 4352/4352 [==============================] - 3s 649us/step - loss: 0.0108 - accuracy: 0.9979
    # Epoch 16/20
    # 4352/4352 [==============================] - 3s 655us/step - loss: 0.0109 - accuracy: 0.9972
    # Epoch 17/20
    # 4352/4352 [==============================] - 3s 654us/step - loss: 0.0100 - accuracy: 0.9977
    # Epoch 18/20
    # 4352/4352 [==============================] - 3s 642us/step - loss: 0.0094 - accuracy: 0.9982
    # Epoch 19/20
    # 4352/4352 [==============================] - 3s 651us/step - loss: 0.0089 - accuracy: 0.9984
    # Epoch 20/20
    # 4352/4352 [==============================] - 3s 654us/step - loss: 0.0099 - accuracy: 0.9977
    # Predictions 1:
    #  [[9.8469555e-03]
    #  [9.9870098e-01]
    #  [1.5222430e-03]
    #  [8.5604170e-06]
    #  [4.1239687e-07]
    #  [9.9999970e-01]
    #  [2.2066997e-06]
    #  [3.7384033e-04]
    #  [9.9867487e-01]
    #  [1.7589033e-03]
    #  [2.2860988e-08]
    #  [3.0502975e-03]
    #  [1.6421080e-04]
    #  [1.0000000e+00]
    #  [8.7380844e-01]]
    # Predictions 2:
    #  [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]
    # Predictions 3:
    #  [0 1 0 0 0 1 0 0 1 0 0 0 0 1 1]
    # 68/68 [==============================] - 0s 612us/step - loss: 0.0232 - accuracy: 0.9958
    # The model score:
    #  [0.023200275376439095, 0.9958041906356812]