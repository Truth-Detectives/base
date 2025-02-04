# Binary Classification Problem

*This notebook investigates three binary classification models on the preprocessed version of the WELFAKE dataset.*
*The models used in this task are Logistic Regression, K-Nearest Neighbor and Naive Bayes.**The dataset used contains 15 columns of data 7 of which contain numerical data that will be used as the feature data for these models as well as 1 category of text data.*
*It is important to note that this dataset uses the value 0 to represent real news and the value 1 to represent fake news.This investigation seeks to compare the accuracy and f1-scores of different models when it comes to fake news detection.*

# Table of contents

- Requirements
- Resources
- Installation
- How to run project
- Preparing the data for logistic regression and k-nearest neighbor
- Logistic Regression
- Scatterplot
- K-Nearest Neighbor
- Preparing the data for Naive Bayes
- Naive Bayes

# Requirements

*This task requires the use of the scikit-learn library including matplotlib, numpy, pandas and seaborn to display mathematical data*

[scikit-learn](https://scikit-learn.org/stable/install.html)
[pandas](https://pypi.org/project/pandas/)
[numpy](https://pypi.org/project/numpy/)
[seaborn](https://pypi.org/project/seaborn/)
[matplotlib](https://pypi.org/project/matplotlib/)

# Resources

*This is the dataset used for this task*
[preprocessed_welfake_dataset](https://www.kaggle.com/datasets/ceasor6/preprocessed-welfake-news-dataset)

# Installation

## Install scikit-learn library

```bash
python -m venv sklearn-env
sklearn-env\Scripts\activate
pip install -U scikit-learn
```
## Install pandas

```bash
pip install pandas
```

## Install numpy

```bash
pip install numpy
```

## Install seaborn

```bash
pip install seaborn
```

## Install matplotlib

```bash
pip install matplotlib
```

# How to Run Project

*In order to run the segments of code. The user must click the necessary cell and then click the play button in the top navigation bar.*

# Preparing the Data for Logistic Regression and K-Nearest Neighbor

*The data was first read through the use of pandas and stored in a variable named pdata. The features that would be used to feed into the models was then identified. The selected features were, punctuation_count,uppercase_ratio,numerical_count,sentiment_polarity,title_len,text_len and total_len*
*After this was done X was set as the feature data and y was set as label data. Then the data was split into testing and training sets with a test size of 25% and a random state of 42.*
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
```
*The data was then scaled using StandarScalar to ensure that all data is on the same scale so that larger scaled variables don't affect the overall accuracy. Once all these stages have been completed the data is now prepared to be fed into the models*

# Logistic Regression

*The logistic regression model is initialized using a max_iter value of 500, since it is a large dataset the number of iterations would need to increase from the default 100, a random state of 42 is also set.*
```python
lrmodel = LogisticRegression(max_iter=500,random_state=42)
```
*The model is then trained with the training sets X_train and y_train. Once the model has been trained the predict() function is used to acquire an array of predicted labels. This array can then be used to generate the classification report and the accuracy of the model. Using the metrics library the confusion matrix can be calculated. Then using matplotlib and seaborn this matrix can be displayed along with the AUC-ROC curve and generated values.*

# Scatterplot

*Scatterplot was used to display the relationships between the length of the articles and varibales such as number count, punctuation count, emotional expressions/tone and capitalizations.*

# K-Nearest Neighbor

*Similarly to Logistic Regression, the model was initialized this time with n_neighbours being set to 10.*
```python
knnmodel = KNeighborsClassifier(n_neighbors=10) 
```
*The model was then trained with the training data and the predicted labels array was generated. The accuracy and classification report was also generated. Using the metrics library the confusion matrix was also calculated and displayed using matplotlib and seaborn. The AUC-ROC values were also calculated and displayed.*

# Preparing the data for Naive Bayes

*The data for the logistic regression and k-nearest neighbor were all done using numerical values as the X data. However for the naive bayes model text data was used as the feature data. The data was then split again using the new X data. After spliting insteading of scaling the data was vectorized using TfidfVectorizer.*

# Naive Bayes
*The multinominal Naives Bayes model was initialized*
```python
nb_classifier = MultinomialNB()
```
*The model was then trained and the label prediction array was generated. The accuracy, classification report and the confusion matrix were also generated and displayed using matplotlib and seaborn. The AUC-ROC values and graph was also calculated and displayed.*