# -*- coding: utf-8 -*-
"""BYOP-SECONDARY-GOAL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rZsGGzT0ODys4J72z4R8XwwISMivBYq_

Importing the necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Dataset Loading(I used the same dataset for secondary goals also for more deep analysis of the data)"""

from google.colab import drive
drive.mount('/content/gdrive')

df = pd.read_csv('/content/gdrive/MyDrive/BYOP/Restaurant_reviews_dataset.csv')

"""Printing the dataset"""

df

"""Dataset Visualisation"""

df.info()

df.describe()

df['Liked'].nunique()

print(df['Liked'].unique())

df['Liked'].value_counts()

df.head()

df.tail()

plt.figure(figsize=(9,5))
sns.countplot(x=df.Liked);

# Generating a correlation matrix of numerical columns
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

"""Defining x & y"""

x=df[' Review'].values
y=df['Liked'].values

"""Splitting the dataset into training & testing datasets"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

"""Viewing the shapes of Training & Testing sets"""

x_train.shape

x_test.shape

y_train.shape

y_test.shape

"""Importing CountVectorizer"""

from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer(stop_words='english')
x_train_vect=vect.fit_transform(x_train)
x_test_vect=vect.transform(x_test)

"""Importing Support Vector Classifier"""

from sklearn.svm import SVC
model=SVC()

"""Training the model"""

model.fit(x_train_vect,y_train)

"""Predicting the test results"""

y_pred=model.predict(x_test_vect)

"""Evaluating the model"""

from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_test)*100

"""Creating Pipelines for the same task"""

from sklearn.pipeline import make_pipeline
text_model=make_pipeline(CountVectorizer(),SVC())

"""Training the model with training sets"""

text_model.fit(x_train,y_train)

"""Predicting the test results"""

y_pred=text_model.predict(x_test)

y_pred

"""Evaluating the Model

```
# This is formatted as code
```


"""

from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_test)*100

"""Saving the Model"""

import joblib
joblib.dump(text_model,'BYOP-SECONDARY-GOAL')

"""# Prediction of New Reviews using our awesome model!"""

text_model.predict(["Super delicious food"])

text_model.predict(["why so salty food"])

"""The next review should have returned 1 but returns 0 indicating the model is not 100% accurate, but still it returns correct integer value for 8 out of 10 reviews i.e 80% accuracy."""

text_model.predict(["Sauce was fresh"])

text_model.predict(["Nice bouffet!"])

