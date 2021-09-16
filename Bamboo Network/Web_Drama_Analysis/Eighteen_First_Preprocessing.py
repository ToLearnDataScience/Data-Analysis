# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 18:24:09 2021

@author: 82108
"""

"""
Eighteen_First_Preprocessing
"""

import pandas as pd
import re
##############################################################################
# like preprocessing

for i in range(1, 25):
    load_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
    dataset = pd.read_csv(load_path+f"Eighteen_First_0{i}.csv", encoding='utf-8-sig')
    
    try:
        idx = dataset[dataset['comment'] == 'None'].index
        dataset.drop(idx, inplace=True)
    except:
        pass
    
    comments_list = list(dataset['comment'])
    comment_likes_list = list(dataset['like'])
            
    num_list = []
    for num in comment_likes_list:
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
    
    dataset_dict = {'comment':comments_list, "like":num_list}
    dataset_pd = pd.DataFrame(dataset_dict)
    save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/Preprocessing/data for basic analysis/"
    dataset_pd.to_csv(save_path+f"Eighteen_First_0{i}_pre_basic.csv", index=False, encoding='utf-8-sig')
    







##############################################################################
# comments + like preprocessing

for i in range(1, 25):
    load_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
    dataset = pd.read_csv(load_path+f"Eighteen_First_0{i}.csv", encoding='utf-8-sig')
    
    try:
        idx = dataset[dataset['comment'] == 'None'].index
        dataset.drop(idx, inplace=True)
    except:
        pass
    
    
    comments_list = list(dataset['comment'])
    comment_likes_list = list(dataset['like'])
    
    first = []
    for comment in comments_list:
        p = re.complie("[^ :0-9ㄱ-ㅎㅏ-ㅣ가-힣]")
        comment = p.sub("", comment)
        first.append(comment)
    
    second = []
    for comment in first:
        p = re.compile("[^ +]")
        comment = p.sub(" ", comment)
        second.append(comment)
    
    third = []
    for comment in second:
        if len(comment) >= 2:
            comment = comment
            third.append(comment)
        else:
            comment = ""
            third.append(comment)
            
    num_list = []
    for num in comment_likes_list:
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
    
    dataset_dict = {'comment':third, "like":num_list}
    dataset_pd = pd.DataFrame(dataset_dict)
    save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
    dataset_pd.to_csv(save_path+f"Eighteen_First_0{i}_pre.csv_all", index=False, encoding='utf-8-sig')
    






##############################################################################
# info preprocessing

load_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
dataset = pd.read_csv(load_path+"Eighteen_First_info.csv", encoding='utf-8-sig')

dataset.info
dataset.columns

title_list = list(dataset['title'])
print(title_list)
view_list = list(dataset['view'])
print(view_list)
comment_number_list = list(dataset['comment_number'])
print(comment_number_list)
like_list = list(dataset['like'])
print(like_list)
dislike_list = list(dataset['dislike'])
print(dislike_list)


view_pre = []
for view in view_list:
    p = re.compile("[^0-9]")
    view = p.sub("", view)
    view_pre.append(view)
print(view_pre)

comment_number_pre = []
for number in comment_number_list:
    p = re.compile("[^0-9]")
    number = p.sub("", number)
    comment_number_pre.append(int(number))
print(comment_number_pre)

like_pre = []
for like in like_list:
    if "." in like and "천" in like:
        like1 = like.replace("천", "00")
        like2 = like1.replace(".", "")
        like_pre.append(int(like2))
    elif "천" in like:
        like1 = like.replace("천", "000")
        like_pre.append(int(like1))
    elif "." in like and "만" in like:
        like1 = like.replace("만", "000")
        like2 = like1.replace(".", "")
        like_pre.append(int(like2))
    elif "만" in like:
        like1 = like.replace("만", "0000")
        like_pre.append(int(like1))
    else:
        print("The number is out of range!")
print(like_pre)

dislike_pre = []
for dislike in dislike_list:
    if "." in dislike and "천" in dislike:
        dislike1 = dislike.replace("천", "00")
        dislike2 = dislike1.replace(".", "")
        dislike_pre.append(int(dislike2))
    elif "천" in dislike:
        dislike1 = dislike.replace("천", "000")
        dislike_pre.append(int(dislike1))
    elif "." in dislike and "만" in dislike:
        dislike1 = dislike.replace("만", "000")
        dislike2 = dislike1.replace(".", "")
        dislike_pre.append(int(dislike2))
    elif "만" in dislike:
        dislike1 = dislike.replace("만", "0000")
        dislike_pre.append(int(dislike1))
    else:
        dislike_pre.append(int(dislike))
print(dislike_pre)


dataset_dict = {'title':title_list, 'view':view_pre, 'comment_number':comment_number_pre, 'like':like_pre, 'dislike':dislike_pre}
dataset_pd = pd.DataFrame(dataset_dict)

save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
dataset_pd.to_csv(save_path+"Eighteen_First_info_pre.csv", index=False, encoding='utf-8-sig')

