# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:46:50 2021

@author: 82108
"""

"""
Eighteen vs Bullies Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt

load_path = "C:/Users/82108/Desktop\Study/BAMBOO/정량적 분석/Eighteen_vs_Bullies/"
eighteen_dataset = pd.read_csv(load_path+"Eighteen_First_info_pre.csv", encoding="utf-8-sig")
bullies_dataset = pd.read_csv(load_path+"Bullies_info_pre.csv", encoding="utf-8-sig")

eighteen_dataset.info()
bullies_dataset.info()


# view graph
count24 = list(range(1,25))
count15 = list(range(1,16))
eighteen_view_list = list(eighteen_dataset["view"])
bullies_view_list = list(bullies_dataset["view"])

plt.bar(count24, eighteen_view_list)
plt.plot(count24, eighteen_view_list, color='red', linestyle="--", marker='o')
plt.xlabel("Episode_No")
plt.ylabel("View")
plt.show()



# comment avg bar graph
plt.bar(count15, bullies_view_list, color="orange")
plt.plot(count15, bullies_view_list, color='blue', linestyle="--", marker='o')
plt.xlabel("Episode_No")
plt.ylabel("View")
plt.show()

eighteen_comment_count_avg = eighteen_dataset["comment_number"].mean()
print(eighteen_comment_count_avg)
bullies_comment_count_avg = bullies_dataset["comment_number"].mean()
print(bullies_comment_count_avg)

plt.bar(["Eighteen", "Bullies"], [eighteen_comment_count_avg, bullies_comment_count_avg],
            color=["cornflowerblue", "orange"])
plt.xlabel("Title")
plt.ylabel("Comment_AVG")
plt.show()



# view avg bar graph
eighteen_view_avg = eighteen_dataset["view"].mean()
print(eighteen_view_avg)
bullies_view_avg = bullies_dataset["view"].mean()
print(bullies_view_avg)

plt.bar(["Eighteen", "Bullies"], [eighteen_view_avg, bullies_view_avg],
            color=["cornflowerblue", "orange"])
plt.xlabel("Title")
plt.ylabel("View_AVG")
plt.show()