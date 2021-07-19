# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:06:12 2021

@author: 82108
"""

"""
Crawling : Web Drama "Love As You Taste" comments 

- To do "Morphological Analysis", I crawled Youtube comments of "Love As You Taste."
- "Love As You Taste" is a web-drama of B-PLAY.
- The web-drama consists of 18 videos (1 teaser, 17 episodes)
- I uploaded the result of this code on my github repositories. (file : Love As You taste.zip)
"""

# import modules to control web page(Chrome)
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

# import modules to do data crawling
from bs4 import BeautifulSoup

'''
# Step 00 : URL
- I gathered URL of web drama "Love As You Taste(18 episodes)."
'''

url_list = ['https://www.youtube.com/watch?v=Z9m5976tvw0&list=PL8g_6wQttkwGTcB2AkNCzZxbERcZMD9C9',
            'https://www.youtube.com/watch?v=MU2MyrNMves',
            'https://www.youtube.com/watch?v=ayR5WIHUznE',
            'https://www.youtube.com/watch?v=Rs7J5CQKkq0&t=1s',
            'https://www.youtube.com/watch?v=hnI3Rs-0_68',
            'https://www.youtube.com/watch?v=ZtDTyEXSTyw',
            'https://www.youtube.com/watch?v=MJqrQtUvZ94&t=1s',
            'https://www.youtube.com/watch?v=iZY51i16y_4',
            'https://www.youtube.com/watch?v=t2x7AaSSkFQ',
            'https://www.youtube.com/watch?v=8Ot9ovkWzYs',
            'https://www.youtube.com/watch?v=_E4neWauaSU&t=1s',
            'https://www.youtube.com/watch?v=qTUlw2aD9E0',
            'https://www.youtube.com/watch?v=2exLyYadpt8',
            'https://www.youtube.com/watch?v=EBSwukFePL0',
            'https://www.youtube.com/watch?v=5p12rqmo8Qk',
            'https://www.youtube.com/watch?v=SXorqvgFgxU',
            'https://www.youtube.com/watch?v=uo_Gj_12f9o',
            'https://www.youtube.com/watch?v=CYguLyWLhZU&t=3s']

'''
# Step 01 : selenium + webdriver
'''

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/chromedriver_win32/"
browser = wd.Chrome(executable_path = path + "chromedriver.exe")


# Step 02 : control Chrome(selenium) + parsing(beautifulsoup)

all_episodes_comments = []

for url in url_list :
    browser.get(url)
    browser.maximize_window()
    
    time.sleep(5)
    
    pause_sec = 2
    
    body = browser.find_element_by_tag_name('body')
    
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    body.send_keys(Keys.PAGE_UP)

    while True:
        last_height = browser.execute_script('return document.documentElement.scrollHeight')
        body.send_keys(Keys.END)
        time.sleep(pause_sec)
        new_height = browser.execute_script('return document.documentElement.scrollHeight')
        if new_height == last_height:
            break;
    
    html_source = browser.page_source
            
    html = BeautifulSoup(html_source, "lxml")
    
    # extracting tag
    tag = html.select('yt-formatted-string#content-text') # comments_tag
    
    # preprocessing(tag)
    episode_comments = []
    
    for t in tag :
        comment = str(t.string)
        episode_comments.append(comment)
    
    all_episodes_comments.append(episode_comments)
    
browser.close()

print(all_episodes_comments)

print(all_episodes_comments[0])
print(all_episodes_comments[1])
print(all_episodes_comments[2])
print(all_episodes_comments[3])
print(all_episodes_comments[4])
print(all_episodes_comments[5])
print(all_episodes_comments[6])
print(all_episodes_comments[7])
print(all_episodes_comments[8])
print(all_episodes_comments[9])
print(all_episodes_comments[10])
print(all_episodes_comments[11])
print(all_episodes_comments[12])
print(all_episodes_comments[13])
print(all_episodes_comments[14])
print(all_episodes_comments[15])
print(all_episodes_comments[16])
print(all_episodes_comments[17])

for i in range(18) :
    with open(f"LAYT{i}.txt", mode = "w", encoding = 'utf-8') as f :
        for j in range(len(all_episodes_comments[i])) :
            comment = all_episodes_comments[i][j]
            f.write(comment)
            f.write("\n")

