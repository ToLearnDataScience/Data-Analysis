# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:35:00 2021

@author: 82108
"""

"""
Morphological Analysis

1) Data Crawling (from New York Times)
2) Morpholgical Analysis(from Obamaspeeches.com / Inaugural Speech)
3) Visualization
"""

"""
Although I practiced data crawling using the data from New York Times, I didn't analyze the data.
This is because I think analyzing the speech of the president Obama is more interesting.
"""

# Step 0 : import module

# modules for Data Crawling
import urllib.request as req # url
from bs4 import BeautifulSoup # parsing

# a module for Morphological Analysis
import nltk # Natural Language Toolkit
from nltk.corpus import stopwords # eliminating stopwords
from nltk.tag import pos_tag

# modules for vizualization
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

'''
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
'''


# Step 1 : Data Crawling

url = "https://www.nytimes.com/section/world"

res = req.urlopen(url)
read_url = res.read()
data = read_url.decode('utf-8') # mostly use "utf-8", but sometimes "cp1252" is used.

html = BeautifulSoup(data, "html.parser")

tag = html.select('h2[class="css-1j9dxys e1xfvim30"]')

latest_news = []

for t in tag :
    sent = str(t.string)
    latest_news.append(sent)

cnt = 0

for l in latest_news :
    cnt += 1
    print(f"{cnt} -> {l}")
    
'''
1 -> Your Thursday Briefing
2 -> Haiti’s political turmoil may hamper efforts to contain the virus, the W.H.O. says.
3 -> California’s Capitol revives a mask rule after an outbreak infected four fully vaccinated people.
4 -> Biden Weighs a Response to Ransomware Attacks
5 -> Former South African President Is Arrested
6 -> A magnet for exploitation: Haiti over the centuries.
7 -> Haitian Ambassador Says Assassination Was By Professionals
8 -> Haiti’s President Is Assassinated
9 -> Your Thursday Briefing
10 -> What is an ‘état de siège’? No one seems quite sure.
'''


# Step 2 : Morphological Analysis

# 1) Loading Data
with open("C:/Jump_to_Python/Practice/Practice_data/obama.txt", "r", encoding = "utf-8") as f :
    data = f.readlines()

print(data)

# 2) Preprocessing Data
count = 0

# remove "\s" or "\n"
for l in data :
    count += 1
    print("{} -> {}".format(count, len(l)))
    
sentences = []

for line in data :
    if len(line) > 1 :
        sentences.append(line.strip())

print(sentences)

# Tokenize
token_list = []

for s in sentences :
    ts = nltk.tokenize.word_tokenize(s)
    token_list.extend(ts)

print(token_list)

# remove stopwords
stop_words = set(stopwords.words('english'))

stop_list = []

for t in token_list :
    if t not in stop_words :
        stop_list.append(t)
        
print(stop_list)

# choose only "Noun", "Verb", and "Adjective"
final_list = []

for word, pos in pos_tag(stop_list) :
    if pos in ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS'] :
        final_list.append(word)

print(final_list)


# Step 3 : Visualization

word_count = Counter(final_list)
Top20_word = word_count.most_common(20)
print(Top20_word)
"""
[('nation', 24), ('new', 22), ('America', 20), ('world', 14), ('work', 12), 
 ('common', 12), ('people', 12), ('today', 10), ('generation', 10), ('day', 10),
 ('time', 10), ('know', 10), ('spirit', 10), ('let', 10), ('words', 8), ('peace', 8),
 ('crisis', 8), ('come', 8), ('end', 8), ('things', 8)]
"""

Word_Cloud = WordCloud(width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')

Word_Result = Word_Cloud.generate_from_frequencies(dict(Top20_word)) 

plt.imshow(Word_Result)
plt.axis("off")
plt.show()    

plt.savefig("ObamaWC.png", dpi=300)















