# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 14:45:04 2021

@author: 82108
"""

Eighteen_Season01_url_list = ["https://www.youtube.com/watch?v=nca7i5oX09o",
                              "https://www.youtube.com/watch?v=XwHgjmRoNc4&t=1s",
                              "https://www.youtube.com/watch?v=c9hSEcmQJa8",
                              "https://www.youtube.com/watch?v=aqjzhyhfC5Q",
                              "https://www.youtube.com/watch?v=nP_JrlpiIIs",
                              "https://www.youtube.com/watch?v=-7vGsE6Hmzc",
                              "https://www.youtube.com/watch?v=yZeLiJN-3Fw",
                              "https://www.youtube.com/watch?v=sGv2lcGcVgs",
                              "https://www.youtube.com/watch?v=SiDXArHH-M4",
                              "https://www.youtube.com/watch?v=8FJIStYn7T0",
                              "https://www.youtube.com/watch?v=5fTP9sEFtvI",
                              "https://www.youtube.com/watch?v=FcU1tTAtPzo",
                              "https://www.youtube.com/watch?v=8Mx6Qyd8GWE",
                              "https://www.youtube.com/watch?v=a6TwTkaxxtM",
                              "https://www.youtube.com/watch?v=BJ1bFKpSBmM",
                              "https://www.youtube.com/watch?v=c8Us36TxoAc",
                              "https://www.youtube.com/watch?v=XEAjJRpjTeI",
                              "https://www.youtube.com/watch?v=PhfTNd-oZo4",
                              "https://www.youtube.com/watch?v=yJUgSwnvaxA",
                              "https://www.youtube.com/watch?v=dfG64hh5LRQ",
                              "https://www.youtube.com/watch?v=lOfQMB8SD_Q",
                              "https://www.youtube.com/watch?v=69tE59Tjz24",
                              "https://www.youtube.com/watch?v=SmqclJ7bIok",
                              "https://www.youtube.com/watch?v=bsLbtmKPGVY",
                              "https://www.youtube.com/watch?v=FFA4pkbtRxg",
                              "https://www.youtube.com/watch?v=ZCbaojdNpS8"]

# modules for crawling
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/chromedriver_win32/"
driver = wd.Chrome(executable_path = path+"chromedriver.exe")

for i in [23, 24]:
    driver.get(Eighteen_Season01_url_list[i])
    driver.maximize_window()
    
    time.sleep(3)
    
    body = driver.find_element_by_tag_name('body')
    
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    body.send_keys(Keys.PAGE_UP)
    
    cnt = 30
    while True:
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        body.send_keys(Keys.END)
        time.sleep(6)
        new_height = driver.execute_script('return document.documentElement.scrollHeight')
        cnt -= 1
        if cnt == 0:
            time.sleep(30)
            cnt = 30
        if new_height == last_height:
            break
    
    try:
        driver.find_element_by_css_selector('#dismiss-button > a')
    except:
        pass
    
    html_source = driver.page_source
    html = BeautifulSoup(html_source, 'lxml')
    
    comment_tags = html.select('yt-formatted-string#content-text')
    comment_like_tags = html.select('span#vote-count-middle')
    
    comments = []
    comment_likes = []
    
    for comment in comment_tags:
        comment = str(comment.text)
        comments.append(comment)
    
    for like in comment_like_tags:
        like = str(like.text)
        comment_likes.append(like)
    
    save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
    
    if i == 0:
        teaser_dict = {'comment':comments, 'like':comment_likes}
        teaser_pd = pd.DataFrame(teaser_dict)
        teaser_pd.to_csv(save_path+"Eighteen_First_teaser.csv", index=False, encoding='utf-8-sig')
    elif i >= 1 and i <= 24:
        episode_dict = {'comment':comments, 'like':comment_likes}
        episode_pd = pd.DataFrame(episode_dict)
        episode_pd.to_csv(save_path+f"Eighteen_First_0{i}.csv", index=False, encoding='utf-8-sig')
    elif i == 25:
        special_dict = {'comment':comments, 'like':comment_likes}
        special_pd = pd.DataFrame(special_dict)
        special_pd.to_csv(save_path+"Eighteen_First_special.csv", index=False, encoding='utf-8-sig')

driver.close()
    




##############################################################################


# save(info)
path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/chromedriver_win32/"
driver = wd.Chrome(executable_path = path+"chromedriver.exe")

titles = []
views = []
likes = []
dislikes = []
comment_counts = []

for url in Eighteen_Season01_url_list:
    driver.get(url)
    driver.maximize_window()
    
    time.sleep(5)
    
    body = driver.find_element_by_tag_name('body')
    
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    body.send_keys(Keys.PAGE_UP)

    
    html_source = driver.page_source
    html = BeautifulSoup(html_source, 'lxml')
    
    title_tag = html.find_all('yt-formatted-string', {'force-default-style':"", 'class':'style-scope ytd-video-primary-info-renderer'})
    title = str(title_tag[0].string)
    video_view_tag = html.find_all('span',{'class':'view-count style-scope ytd-video-view-count-renderer'})
    view = str(video_view_tag[0].string)
    like_num_tag = html.find_all('yt-formatted-string',{'id':'text', 'class':'style-scope ytd-toggle-button-renderer style-text', 'aria-label':re.compile("좋아요")})
    like = str(like_num_tag[0].string)
    dislike_num_tag = html.find_all('yt-formatted-string',{'id':'text', 'class':'style-scope ytd-toggle-button-renderer style-text', 'aria-label':re.compile("싫어요")})
    dislike = str(dislike_num_tag[0].string)
    comment_count_tag = html.find_all('h2', {'id':'count', 'class':'style-scope ytd-comments-header-renderer'})
    comment_count = str(comment_count_tag[0].text)
    
    titles.append(title)
    views.append(view)
    likes.append(like)
    dislikes.append(dislike)
    comment_counts.append(comment_count)

driver.close()

Eighteen_First_dict = {'title':titles, 'view':views, 'comment_number':comment_counts, 'like':likes, 'dislike':dislikes}
Eighteen_First_pd = pd.DataFrame(Eighteen_First_dict)
Eighteen_First_pd.head()

save_path = "C:/Users/82108/Desktop/Study/BAMBOO/정량적 분석/Eighteen/comments_without_more/"
Eighteen_First_pd.to_csv(save_path+"Eighteen_First_info.csv", index=False, encoding='utf-8-sig')













    
    
    
    
    
    
    
    