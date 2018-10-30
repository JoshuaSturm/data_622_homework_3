'''
DATA 622 - Homework 2
Joshua Sturm
10/07/2018

This script will clean and and impute data in the files we downloaded.
It will then fit a random forest classification model to the data, and save (pickle) it.
'''

# Import libraries
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Import testing and training files
train_raw = pd.read_csv('train.csv')
test_raw = pd.read_csv('test.csv')

# Check for missing data
train_raw.isnull().sum()

# Check percentage of missing rows
round(train_raw['Cabin'].isnull().sum()/train_raw.shape[0], 2) * 100

'''
Since such a large portion of the cabin column is missing values, we can remove it from both datasets,
and omit it from our model.
Additionally, since there are so many unique values for 'Name' and 'Ticket', we can remove those as well.
Lastly, PassengerId serves no purpose, so we can drop it.
'''
train = train_raw.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1)
test = test_raw.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1)

'''
Following the advice from this website (https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4), we can
remove the two rows in the 'Embarked' column, since they are likely missing at random, and therefore won't introduce
any bias into our model.

We will do the same for the 'Fare' column in the testing dataset.
'''
train = train[pd.notnull(train['Embarked'])]
test = test[pd.notnull(test['Fare'])]

'''
Convert nominal categories 'Embarked', 'Sex', and 'Survived' to categorical
'''
# train[['Embarked', 'Sex', 'Survived']] = train[['Embarked', 'Sex', 'Survived']].apply(lambda x: x.astype('category'))
# test[['Embarked', 'Sex']] = test[['Embarked', 'Sex']].apply(lambda x: x.astype('category'))

'''
Convert categorical variables 'Sex' and 'Embarked' to dummies (binary)
'''
train = pd.get_dummies(train, columns = ['Sex', 'Embarked'], drop_first = True)
test = pd.get_dummies(test, columns = ['Sex', 'Embarked'], drop_first = True)

'''
Convert ordinal columns 'Age', 'Parch', 'Pclass', and 'SibSp' to categorical, and preserve order
'''

# train['Pclass'] = pd.Categorical(train.Pclass, ordered = True, categories = [1, 2, 3])
# test['Pclass'] = pd.Categorical(test.Pclass, ordered = True, categories = [1, 2, 3])

'''
-------------------------------------------------
Impute age, build model
'''
train['Age'] = train['Age'].fillna('NaN')
test['Age'] = test['Age'].fillna('NaN')

steps = [('imputation', SimpleImputer(missing_values = 'NaN', strategy = 'most_frequent')),
         ('random_forest', RandomForestClassifier())]
pipeline = Pipeline(steps)

X = train.drop('Survived', axis = 1)
y = train['Survived']

# Split data to create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the pipeline to the train set
rfmodel = pipeline.fit(X_train, y_train)

'''
Save (pickle) the random forest model
'''
random_forest_pkl = 'titanic_random_forest.pkl'

# Open the file to save as pkl file
rf_pkl = open(random_forest_pkl, 'wb')
pickle.dump(rfmodel, rf_pkl)

# Close the pickle instances
rf_pkl.close()


'''
References:
- http://dataaspirant.com/2017/02/13/save-scikit-learn-models-with-python-pickle/
'''