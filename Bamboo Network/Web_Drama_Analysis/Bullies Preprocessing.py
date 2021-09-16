# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:42:33 2021

@author: 82108
"""

"""
When you're on the blacklist of bullies Data Preprocessing
"""

import pandas as pd
import re

pd.set_option("display.max_rows", 1000)


# save comments with Time Stamp
load_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/When you're on the blacklist of bullies/data/raw data/"
dataset = pd.read_csv(load_path+"bullies015.csv", encoding='utf-8-sig')

dataset.info()
dataset.head()

include_minutes = dataset["comment"].str.contains(r"\d+:\d+")
minutes_df = dataset[include_minutes].sort_values(by="like", ascending=False)
print(minutes_df)


# preprocessing
comment_list = list(minutes_df['comment'])
like_list = list(minutes_df['like'])
print(len(comment_list))
print(len(like_list))

for n in like_list:
    num_list = []
    for num in like_list:
        if "." in num and "천" in num:
            num1 = num.replace(".", "")
            num2 = num1.replace("천", "00")
            num_list.append(int(num2))
        elif "천" in num:
            num1 = num.replace("천", "000")
            num_list.append(int(num1))
        elif "." in num and "만" in num:
            num1 = num.replace(".", "")
            num2 = num1.replace("만", "000")
            num_list.append(int(num2))
        elif "만" in num:
            num1 = num.replace("만", "0000")
            num_list.append(int(num1))
        else:
            num_list.append(int(num))
    
    dataset_dict = {'comment':comment_list, "like":num_list}
    dataset_pd = pd.DataFrame(dataset_dict)

save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/When you're on the blacklist of bullies/data/minute_mark_data/"
dataset_pd.to_csv(save_path+"bullies015_minutes.csv", index=False, encoding='utf-8-sig')


# check the Time Line
load_path2 = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/When you're on the blacklist of bullies/data/minute_mark_data/"
minutes = pd.read_csv(load_path2+"bullies015_minutes.csv", encoding='utf-8-sig')

comment_list = list(minutes['comment'])

minute_list = []
for comment in comment_list:
    m = re.findall(r"\d+:\d+", comment)
    minute_list.extend(m)
    
minute_list.sort()


keyword = input("키워드를 입력하시오. : ")
print("#"*100)
the_keyword = minutes["comment"].str.contains(keyword)
keyword_df = minutes[the_keyword].sort_values(by = "like", ascending=False)
print(keyword_df)
print("#"*100)
print("Count :", len(keyword_df))
print("#"*100)


print(minute_list)
