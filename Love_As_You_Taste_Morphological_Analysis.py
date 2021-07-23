# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:34:23 2021

@author: 82108
"""


"""
Morphological Analysis
"""

# Step 01 : Data Load

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/Love As You Taste/"

all_comments = []

for i in range(18) :
    with open(path + f"LAYT{i}.txt", mode = "r", encoding = 'utf-8') as f :
        data = f.readlines()
        all_comments.append(data)

len(all_comments) # 18
len(all_comments[0]) # 735
print(all_comments[0])


# Step 02 : Preprocessing

pre_all_comments = []

for i in range(18) :
    for j in range(len(all_comments[i])) :
        comment = all_comments[i][j]
        pre_comment = comment.strip()
        pre_all_comments.append(pre_comment)

len(pre_all_comments) # 8274

print(pre_all_comments[:100])


eliminate_none = []

for i in range(len(pre_all_comments)) :
    not_none = pre_all_comments[i]
    if not_none != 'None' :
        eliminate_none.append(not_none)

print(eliminate_none[:100])


# Step 03 : Morphological Analysis

from konlpy.tag import Okt # Module for doing Morphological analysis for Korean

okt = Okt()


ex_pos = []

for comment in eliminate_none :
    pos = okt.pos(comment)
    ex_pos.extend(pos)

noun_adjective = []

for word, word_class in ex_pos :
    if word_class == 'Noun' or word_class == 'Adjective' :
        noun_adjective.append(word)


none_alone = []

for word in noun_adjective :
    if len(word) >= 2 :
        none_alone.append(word)


# Step 04 : Count

from collections import Counter

word_count = Counter(none_alone)

Top25 = word_count.most_common(25)


# Step 05 : Visualization

from wordcloud import WordCloud
import matplotlib.pyplot as plt


Word_Cloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
                       width=500, height=400, 
                       max_words=100,max_font_size=150, 
                       background_color='white')

Word_Result = Word_Cloud.generate_from_frequencies(dict(Top25))

path2 = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/"

plt.imshow(Word_Result)
plt.axis("off")
plt.savefig(path2 + "LAYT.png", dpi=300)
plt.show()   









