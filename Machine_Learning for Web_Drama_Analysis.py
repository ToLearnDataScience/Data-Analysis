# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:57:23 2021

@author: 82108
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



# Step01 : Data Load

import os

os.chdir(r"C:\Users\82108\Desktop\Study\Educational Background\Programming\개인 공부\★_Github\Data_Analysis\Movie_Comments_Sentimental_Analysis")

train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')



# Step02 : Data Preprocessing

len(train_data) # 150000
len(test_data) # 50000

train_data.drop_duplicates(subset = ['document'], inplace=True) 
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") 
train_data['document'] = train_data['document'].str.replace('^ +', "") 
train_data['document'].replace('', np.nan, inplace=True) 
train_data = train_data.dropna(how='any') 

test_data.drop_duplicates(subset = ['document'], inplace=True) 
test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") 
test_data['document'] = test_data['document'].str.replace('^ +', "") 
test_data['document'].replace('', np.nan, inplace=True) 
test_data = test_data.dropna(how='any') 

len(train_data) # 145393
len(test_data) # 48852



# Step03 : Tokenize

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

okt = Okt()

X_train = []

for sentence in train_data['document'] :
    X1 = okt.morphs(sentence, stem=True)
    X2 = [word for word in X1 if not word in stopwords]
    X_train.append(X2)
    

X_test = []

for sentence in test_data['document'] :
    X1 = okt.morphs(sentence, stem=True)
    X2 = [word for word in X1 if not word in stopwords]
    X_test.append(X2)


tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

print(tokenizer.word_index)

threshold = 3
total_cnt = len(tokenizer.word_index)
rare_cnt = 0
total_freq = 0
rare_freq = 0

for key, value in tokenizer.word_counts.items() :
    total_freq += value
    
    if value < threshold :
        rare_cnt += 1
        rare_freq += value

print("the size of vocabulary :", total_cnt)
# the size of vocabulary : 43752
print("the words that appears 2 times or less :", rare_cnt)
# the words that appears 2 times or less : 24337
print("the ratio of rare words :", rare_cnt / total_cnt)
# the ratio of rare words : 0.5562488571950996 -> about 56%
print("the rare words occurrence rate :", rare_freq / total_freq)
# the rare words occurrence rate : 0.018715872104872903 -> about 2%
vocab_size = total_cnt - rare_cnt + 1
print("the size of vocabulary except for rare words :", vocab_size)
# the size of vocabulary except for rare words : 19416

tokenizer = Tokenizer(vocab_size) 
tokenizer.fit_on_texts(X_train)
X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

y_train = np.array(train_data['label'])
y_test = np.array(test_data['label'])


# Eliminate empty samples
drop_train = [index for index, sentence in enumerate(X_train) if len(sentence) < 1]
X_train = np.delete(X_train, drop_train, axis=0)
y_train = np.delete(y_train, drop_train, axis=0)



# Step04 : Padding

plt.hist([len(s) for s in X_train], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
plt.show()
max_len = 30

X_train = pad_sequences(X_train, maxlen = max_len)
X_test = pad_sequences(X_test, maxlen = max_len)  



# Step05 : Machine Learning

from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint  
  
model = Sequential()
model.add(Embedding(vocab_size, 100))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))
  
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
mc = ModelCheckpoint('best_model.h5', monitor='val_acc', mode='max', verbose=1, save_best_only=True)
  
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=15, callbacks=[es, mc], batch_size=60, validation_split=0.2)

'''
Epoch 00009: val_acc did not improve from 0.85833
Epoch 00009: early stopping
'''

loaded_model = load_model('best_model.h5')
loaded_model.evaluate(X_test, y_test)[1] # 0.8536804914474487



# Step06 : Sentiment Predict

def sentiment_predict(new_text) :
    first = okt.morphs(new_text, stem=True)
    second = [word for word in first if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([second])
    pad = pad_sequences(encoded, maxlen=max_len)
    score = float(loaded_model.predict(pad))
    if score > 0.5 :
        result = 'positive'
    else :
        result = 'negative'
    return result



# Step07 : Web Drama Data Load + Analysis

# 1) Love As You Taste

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/Love As You Taste/"

LAYT_comments = []

for i in range(18) :
   with open(path + f"LAYT{i}.txt", mode = "r", encoding = "utf-8") as f :
       data = f.readlines()
       LAYT_comments.extend(data)

len(LAYT_comments) # 8274


# Eliminate "None"

LAYT_eli_none = []

for com in LAYT_comments :
    if com.strip() != "None" :
        LAYT_eli_none.append(com)

len(LAYT_eli_none) # 7275


# Drama Rating

LAYT_react = []

for comment in LAYT_eli_none :
    LAYT_react.append(sentiment_predict(comment))

LAYT_react_ratio = LAYT_react.count("positive") / len(LAYT_react)
print(LAYT_react_ratio) 
# 0.4988316151202749


# Actor Rating

LAYT_act_react = []

for comment in LAYT_eli_none :
    if "배우" in comment or "연기" in comment :
        LAYT_act_react.append(comment)

len(LAYT_act_react) # 210

LAYT_act = []

for comment in LAYT_act_react :
    LAYT_act.append(sentiment_predict(comment))

LAYT_act_ratio = LAYT_act.count("positive") / len(LAYT_act)
print(LAYT_act_ratio) # 0.6428571428571429


# 2) The Sweet Blood

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/The Sweet Blood/"

TSB_comments = []

for i in range(17) :
   with open(path + f"TSB{i}.txt", mode = "r", encoding = "utf-8") as f :
       data = f.readlines()
       TSB_comments.extend(data)

len(TSB_comments) # 690

# Eliminate "None"

TSB_eli_none = []

for com in TSB_comments :
    if com.strip() != "None" :
        TSB_eli_none.append(com)

len(TSB_eli_none) # 582


# Drama Rating

TSB_react = []

for comment in TSB_eli_none :
    TSB_react.append(sentiment_predict(comment))

TSB_react_ratio = TSB_react.count("positive") / len(TSB_react)
print(TSB_react_ratio) # 0.44501718213058417


# Actor Rating

TSB_act_react = []

for comment in TSB_eli_none :
    if "배우" in comment or "연기" in comment :
        TSB_act_react.append(comment)

len(TSB_act_react) # 23

TSB_act = []

for comment in TSB_act_react :
    TSB_act.append(sentiment_predict(comment))

TSB_act_ratio = TSB_act.count("positive") / len(TSB_act)
print(TSB_act_ratio) # 0.5652173913043478


# 3) The Witch Store

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/The Witch Store/"

TWS_comments = []

for i in range(12) :
   with open(path + f"TWS{i}.txt", mode = "r", encoding = "utf-8") as f :
       data = f.readlines()
       TWS_comments.extend(data)

len(TWS_comments) # 5711


# Eliminate "None"

TWS_eli_none = []

for com in TWS_comments :
    if com.strip() != "None" :
        TWS_eli_none.append(com)

len(TWS_eli_none) # 4729


# Drama Rating

TWS_react = []

for comment in TWS_eli_none :
    TWS_react.append(sentiment_predict(comment))

TWS_react_ratio = TWS_react.count("positive") / len(TWS_react)
print(TWS_react_ratio) # 0.40579403679424825


# Actor Rating

TWS_act_react = []

for comment in TWS_eli_none :
    if "배우" in comment or "연기" in comment :
        TWS_act_react.append(comment)

len(TWS_act_react) # 145

TWS_act = []

for comment in TWS_act_react :
    TWS_act.append(sentiment_predict(comment))

TWS_act_ratio = TWS_act.count("positive") / len(TWS_act)
print(TWS_act_ratio) # 0.6275862068965518


# 4) Secret Crushes

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/Secret Crushes/"

SC_comments = []

for i in range(23) :
   with open(path + f"SC{i}.txt", mode = "r", encoding = "utf-8") as f :
       data = f.readlines()
       SC_comments.extend(data)

len(SC_comments) # 6255


# Eliminate "None"

SC_eli_none = []

for com in SC_comments :
    if com.strip() != "None" :
        SC_eli_none.append(com)

len(SC_eli_none) # 5880


# Drama Rating

SC_react = []

for comment in SC_eli_none :
    SC_react.append(sentiment_predict(comment))

SC_react_ratio = SC_react.count("positive") / len(SC_react)
print(SC_react_ratio) # 0.5644557823129251


# Actor Rating

SC_act_react = []

for comment in SC_eli_none :
    if "배우" in comment or "연기" in comment :
        SC_act_react.append(comment)

len(SC_act_react) # 248

SC_act = []

for comment in SC_act_react :
    SC_act.append(sentiment_predict(comment))

SC_act_ratio = SC_act.count("positive") / len(SC_act)
print(SC_act_ratio) # 0.6048387096774194



# Step08 : Visualization

# 1) Drama Rating Visualization

drama_name = ["LAYT", "TWS", "TBS", "SC"]
drama_rating = [0.50, 0.41, 0.45, 0.56]
actor_rating = [0.64, 0.62, 0.56, 0.60]

drama_series = pd.Series(drama_rating)
drama_scaling = (drama_series-0.3)*2

actor_series = pd.Series(actor_rating)
actor_scaling = (actor_series-0.5)*2


plt.bar(drama_name, drama_scaling, color=['g', 'y', 'r', 'b'])
plt.show()


# 2) Actor Rating Visualization

plt.bar(drama_name, actor_scaling, color=['g', 'y', 'r', 'b'])
plt.show()















