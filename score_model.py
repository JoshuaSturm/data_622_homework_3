'''
DATA 622 - Homework 2
Joshua Sturm
10/07/2018

This script will score the classification model.
'''

import train_model
import pandas as pd
from sklearn.metrics import classification_report
import pickle

# Rename variables
X = train_model.X
y = train_model.y
test = train_model.test
X_test = train_model.X_test
y_test = train_model.y_test
pipeline = train_model.pipeline

# Load pickled model
import_model = open('titanic_random_forest.pkl', 'rb')
model = pickle.load(import_model)


# Use the model to predict on the testing set (split from training set)
y_pred = model.predict(X_test)

# Compute metrics
classification = classification_report(y_test, y_pred)
score = model.score(X_test, y_test)

# Save to txt file
with open('results.txt', 'w') as f:
    f.write(classification)
    f.close()


# Use the model to predict on the testing dataset, and output to csv
test_pred = model.predict(test)
pred_results = pd.DataFrame(test_pred)
pred_results.to_csv('test_predicted.csv')

'''
References:
- http://dataaspirant.com/2017/02/13/save-scikit-learn-models-with-python-pickle/
- https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
- https://pip.pypa.io/en/stable/reference/pip_freeze/
'''
