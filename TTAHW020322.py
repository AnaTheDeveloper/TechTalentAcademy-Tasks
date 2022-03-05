# Task 1
# Select one or more choices from the list of common Machine Learning Algorithms, do some investigations and write me
# a short summary. I am looking for the following:
# • 1. Is it Supervised/Unsupervised/Reinforcement learning?
# • 2. What does the algorithm do?
# • 3. In which situations will it be most useful?
# • 4. (Optional) Can you find any examples of where this algorithm has been used?

# • Linear Regression
# • Logistic Regression
# • Decision Tree
# • SVM (Support Vector Machine)
# • Naive Bayes
# • KNN (K- Nearest Neighbours)
# • K-Means
# • Random Forest

#----------------------------- Task One Completed Below-----------------------------------------#

# 1. The Decision Tree is part of the Classification Algorithm that falls under Supervised Learning in Machine Learning.
# 2. Decision Tree is a tree-like graph where sorting starts from the root node to the leaf node until the target is achieved.
# 3. Adv: - It takes consideration of each possible outcome of a decision and traces each node to the conclusion accordingly.
#         - Decision Tree is one of the easier and reliable algorithms as it has no complex formulae or data structures.
#         - Decision Trees assign a specific value to each problem, decision, and outcome(s). It reduces uncertainty and
#           ambiguity and also increases clarity.
#    Dis: - Decision trees are less appropriate for estimation and financial tasks where we need an appropriate values.
#         - While working with continuous variables, Decision Tree is not fit as the best solution as it tends to lose
#           information while categorizing variables.
#4. Decision Trees could be used in emergency rooms to prioritize patient care (based on factors such as age, gender, symptoms, etc.)

# Task 2
# From this website select follow and complete the Linear Regression Model.
# https://stackabuse.com/linear-regression-in-python-with-scikit-learn/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

if __name__ == '__main__':


    dataset = pd.read_csv('D:\Documents\Tech Talent Academy Bootcamp\student_scores.csv')
    # View all data.
    print("My imported Data set looks like this: \n", dataset)
    # Find how many rows and columns there are.
    print("My dataset has these rows and columns: ", dataset.shape)
    # Using head() to print out the top 5 pieces of data.
    print("The top 5 pieces of data: \n", dataset.head())
    # See the statistical details of the dataset using describe().
    print("The statistical details: \n", dataset.describe())

    # Plot Data
    dataset.plot(x='Hours', y='Scores', style='o')
    plt.title('Hours vs Percentage')
    plt.xlabel('Hours Studied')
    plt.ylabel('Percentage Score')
    plt.show()

    # Divide the data into "attributes" and "labels".
    # Attributes are the independent variables while labels are dependent variables whose values are to be predicted.

    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values

    #  Split this data into training and test sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # Splits 80% of the data to training set while 20% of the data to test set. The test_size variable is where we
    # actually specify the proportion of test set.

    # Time to train our algorithm.
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # To retrieve the intercept:
    print("The value of the intercept and slop calculated by the linear regression algorithm for our dataset: ", regressor.intercept_)

    # Retrieving the slope (coefficient of x):
    print("Retrieving the slope: ", regressor.coef_)

    #  Predictions on the test data.
    y_pred = regressor.predict(X_test)

    #  Compare the actual output values for X_test with the predicted values.
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print("Compare actual output with predicted values: \n", df)

    # Evaluate the performance of algorithm.
    # For regression algorithms, three evaluation metrics are commonly used:
    # Mean Absolute Error (MAE) is the mean of the absolute value of the errors. It is calculated as: MAE = (1/n) * Σ|yi – xi|
    # Mean Squared Error (MSE) is the mean of the squared errors and is calculated as: MSE = Σ (P i – O i) 2 / n
    # Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors: RMSE = √Σ (Pi – Oi)2 / n
    # The Scikit-Learn library comes with pre-built functions that can be used to find out these values for us.

    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    #----------------------------------------FOR GRAPH PLEASE SEE GIT READ ME---------------------------------------#

    # In the above we performed linear regression involving two variables. Almost all real world problems
    # that you are going to encounter will have more than two variables. Linear regression involving multiple variables
    # is called "multiple linear regression". The steps to perform multiple linear regression are almost similar to
    # that of simple linear regression. The difference lies in the evaluation. You can use it to find out which factor
    # has the highest impact on the predicted output and how different variables relate to each other.

    # https://stackabuse.com/linear-regression-in-python-with-scikit-learn/


    # -------------------------TERMINAL OUTPUT----------------------------#

    # My imported Data set looks like this:
    #      Hours  Scores
    # 0     2.5      21
    # 1     5.1      47
    # 2     3.2      27
    # 3     8.5      75
    # 4     3.5      30
    # 5     1.5      20
    # 6     9.2      88
    # 7     5.5      60
    # 8     8.3      81
    # 9     2.7      25
    # 10    7.7      85
    # 11    5.9      62
    # 12    4.5      41
    # 13    3.3      42
    # 14    1.1      17
    # 15    8.9      95
    # 16    2.5      30
    # 17    1.9      24
    # 18    6.1      67
    # 19    7.4      69
    # 20    2.7      30
    # 21    4.8      54
    # 22    3.8      35
    # 23    6.9      76
    # 24    7.8      86
    # My dataset has these rows and columns:  (25, 2)
    # The top 5 pieces of data:
    #     Hours  Scores
    # 0    2.5      21
    # 1    5.1      47
    # 2    3.2      27
    # 3    8.5      75
    # 4    3.5      30
    # The statistical details:
    #             Hours     Scores
    # count  25.000000  25.000000
    # mean    5.012000  51.480000
    # std     2.525094  25.286887
    # min     1.100000  17.000000
    # 25%     2.700000  30.000000
    # 50%     4.800000  47.000000
    # 75%     7.400000  75.000000
    # max     9.200000  95.000000
    #The value of the intercept and slop calculated by the linear regression algorithm for our dataset:  2.0181600414346974
    # Retrieving the slope:  [9.91065648]
    # Compare actual output with predicted values:
    #     Actual  Predicted
    # 0      20  16.884145
    # 1      27  33.732261
    # 2      69  75.357018
    # 3      30  26.794801
    # 4      62  60.491033
    #Mean Absolute Error: 4.183859899002975
    #Mean Squared Error: 21.598769307217406
    #Root Mean Squared Error: 4.647447612100367
