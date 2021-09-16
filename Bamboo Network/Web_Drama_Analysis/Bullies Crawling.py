# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:52:14 2021

@author: 82108
"""

"""
When you're on the blacklist of bullies Data Crawling
"""

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


url_list = ['https://www.youtube.com/watch?v=ok9sgJtaIvY',
            'https://www.youtube.com/watch?v=r41HwBSbFtY&t=7s',
            'https://www.youtube.com/watch?v=u8v26gNYjsY',
            'https://www.youtube.com/watch?v=cKrhg8K7qvc',
            'https://www.youtube.com/watch?v=SCV-XzNCHJA',
            'https://www.youtube.com/watch?v=05AhJjsLB3c',
            'https://www.youtube.com/watch?v=qSTuRLPcpw8',
            'https://www.youtube.com/watch?v=dGtuEt9BNlQ',
            'https://www.youtube.com/watch?v=uV8h_gfrWn8',
            'https://www.youtube.com/watch?v=fdnD1RlD5ho',
            'https://www.youtube.com/watch?v=JafgQXJfV9w',
            'https://www.youtube.com/watch?v=U0rZfCVf8h4',
            'https://www.youtube.com/watch?v=DMJpq8u_x7c',
            'https://www.youtube.com/watch?v=0DbXwisBq8M',
            'https://www.youtube.com/watch?v=OnKob7XjGfQ',
            ]


driver_path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/"
driver = wd.Chrome(executable_path = driver_path + 'chromedriver.exe')

for i in [12]:
    url = url_list[i-1]
    driver.get(url)
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
        time.sleep(5)
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
    
    comment_tag = html.select('yt-formatted-string#content-text')
    comment_like_tag = html.select('span#vote-count-middle')
    
    comment_list = []
    like_list = []
    
    for comment in comment_tag:
        comment = str(comment.text)
        comment_list.append(comment)
    
    for like in comment_like_tag:
        like = str(like.text)
        like_list.append(like)
        
    save_path = "C:/Users\82108/Desktop/Study/BAMBOO/정량적 분석/When you're on the blacklist of bullies/data/raw data/"
    
    bullies_dict = {'comment':comment_list, 'like':like_list}
    bullies_pd = pd.DataFrame(bullies_dict)
    bullies_pd.to_csv(save_path+f"bullies0{i}.csv", index=False, encoding = 'utf-8-sig')
    
driver.close()
        

len(comment_list)
len(like_list)
print(like)
