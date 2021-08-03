# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 12:26:17 2021

@author: 82108
"""

"""
predict UCLA grad admission result 
- Logistic Regression

source : Kaggle.com
"""

# Step01 : load data
import pandas as pd

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/Regression(UCLA_grad)/"
dataset = pd.read_csv(path + "UCLA_grad.csv")


# Step02 : check dataset
dataset.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Serial No.         500 non-null    int64  
 1   GRE Score          500 non-null    int64  
 2   TOEFL Score        500 non-null    int64  
 3   University Rating  500 non-null    int64  
 4   SOP                500 non-null    float64
 5   LOR                500 non-null    float64
 6   CGPA               500 non-null    float64
 7   Research           500 non-null    int64  
 8   Chance of Admit    500 non-null    float64
dtypes: float64(4), int64(5)
memory usage: 35.3 KB
'''
print(len(dataset)) # 500


col_names = list(dataset.columns)
print(col_names)
# ['Serial No.', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research', 'Chance of Admit ']

num_dataset = dataset[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research', 'Chance of Admit ']]

import matplotlib.pyplot as plt

num_dataset.hist(bins=50, figsize=(20,15))
plt.show()


# Step04 : Binary Classification
data_input = dataset[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA']]
data_target = dataset['Chance of Admit ']
type(data_target) # pandas.core.series.Series

import numpy as np
target_list = np.array(data_target.tolist())
print(target_list[:20])
'''
[0.92 0.76 0.72 0.8  0.65 0.9  0.75 0.68 0.5  0.45 0.52 0.84 0.78 0.62
 0.61 0.54 0.66 0.65 0.63 0.62]
'''

binary_target = ["admitted" if chance >= 0.7 else "rejected" for chance in target_list]
print(binary_target[:10])
'''
['admitted', 'admitted', 'admitted', 'admitted', 'rejected', 'admitted', 'admitted', 'rejected', 'rejected', 'rejected']
'''


# Step05 : Split
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data_input, binary_target, test_size = 0.2, random_state = 42)

print(len(train_input), len(test_input)) # 400 100


# Step06 : Standardization
from sklearn.preprocessing import StandardScaler
sd = StandardScaler()
sd.fit(train_input)
train_scaled = sd.transform(train_input)
test_scaled = sd.transform(test_input)


# Step07 : Logistc Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter = 1000, C = 10)
lr.fit(train_input, train_target)
print(lr.score(train_input, train_target)) # 0.88
print(lr.score(test_input,test_target)) # 0.87


# Input my score
prediction = lr.predict([[325, 106, 3, 4.5, 4.0, 7.75]])
print(prediction) # ['admitted']














