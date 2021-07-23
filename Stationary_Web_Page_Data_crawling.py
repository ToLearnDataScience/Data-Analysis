# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:56:22 2021

@author: 82108
"""

"""
Crawling Data from the "Korea Herald" homepage.

- scope : 1~10 page of "Latest News"
"""

# First Step : import modules

import urllib.request as req # url
from bs4 import BeautifulSoup # parsing

"""
The role of "BeautifulSoup"
- pulling data out of HTML and XML files.
"""


# Second Step : Making URL list

URL_list = []

for i in range(1, 11) :
    url = f"http://www.koreaherald.com/list.php?ct=020000000000&np={i}&mp=1"
    URL_list.append(url)
    
# Check
print(URL_list)
'''
['http://www.koreaherald.com/list.php?ct=020000000000&np=1&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=2&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=3&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=4&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=5&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=6&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=7&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=8&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=9&mp=1', 
 'http://www.koreaherald.com/list.php?ct=020000000000&np=10&mp=1']
'''


# Third Step : Making Crawling Function

def Crawling_func(url) :
    
    # url
    request = req.urlopen(url)
    read_url = request.read()
    data = read_url.decode("utf-8")
    
    # parsing
    html = BeautifulSoup(data, "html.parser")
    
    # exracting tag
    tag = html.select('div[class="main_l_t1"]')
    
    page_news = []
    for t in tag :
        cont = str(t.string)
        page_news.append(cont)
        
    return page_news
        

# Final Step : Using the function to crawl Data from the "Korea Herald"

Latest_news = []

for url in URL_list :
    try : 
        page_news = Crawling_func(url)
        Latest_news.append(page_news)
    except :
        print(f"There is no URL({url})")
        
print(Latest_news)

"""
[['[News Focus] Competition heats up for a share of noise-canceling earbud market', 
  '[Newsmaker] Opposition talks about scrapping Ministry of Gender Equality', 
  'Authorities tighten grip on financial crimes using fintech platform, crypto', 
  '[Today’s K-pop] Stray Kids’ new single debuts as No. 1 on Billboard world chart', 
  'Huons acquires marketing rights for Sputnik Light in S. Korea', 
  'Hyundai Card rolls out credit card for Genesis owners', 
  'More young people start businesses amid sluggish job market: data', 
  'LG Electronics Q2 operating profit reaches W1.1tr, up 65.5%', 
  '19 USFK-affiliated individuals test positive for COVID-19', 
  'One K League match postponed following positive COVID-19 case', 
  'Busan tests potential as blockchain industry hub', 
  'Culture Ministry plans new building to house Lee Kun-hee collection', 
  'Giving Korean work a place in global literature', 
  'More Korean film productions join multinational projects', 
  'Volleyball star Kim Yeon-koung, 
  teen swimmer Hwang Sun-woo named S. Korean flag-bearers at Tokyo Olympics'], 
  ['Samsung Electronics projects record W63tr in Q2 sales', 
   'Seoul stocks dip amid virus woes, Kosdaq at another high', 
   'Hyundai Motor, Kia pledge to 100% renewable energy by 2050', 
   'Newly enlisted soldiers can receive Pfizer starting next week: KDCA', 
   'Peonies in all their fragrant glory explored at National Palace Museum show', 
   'Samsung to switch all company cars to eco-friendly vehicles by 2030', 
   'Korea in early days of 4th wave as cases near record high: authorities', 
   'Justice ministry pushes to grant long-term stay permit to foreign talent', 
   'Government action needed to help local firms catch up with global transition to clean energy', 
   'S&P; raises Korea‘s growth outlook for 2021 to 4%', 
   'UNC temporarily suspends tours to Panmunjom over COVID-19 concerns', 
   'Seoul to reduce bus, subway schedules by 20% after 10 p.m.', 
   'COVID-19 resurgence halts entertainment industry', 
   'Civil servant fined for lying about visits to COVID-19-hit facilities', 
   'Special counsel for Park Geun-hye case resigns amid bribery allegations'], 
  ["S. Korea's intelligence agency dismisses rumors over NK leader's health as 'groundless'", 
   '[Seoul Struggles 10] A hostile city for eco-friendly cars', "S. Korea's OTC market value passes W22tr", 
   'LG Electronics expects solid Q2 earnings on home appliance biz', 
   '[Herald Interview] Uncovering ‘true picture’ of Japan’s colonial rule of Korea', 
   'Players on fringe determined to help Olympic football team any way they can', 
   'Critics discount ruling party’s olive branch to North Korea', 
   "S. Korea's REIT market grows 22% in 2020", 'Former top auditor expresses will to join politics', 
   'Economic recovery may lose steam due to spiking COVID-19 cases: KDI', 
   "N. Korea in 'tug of war' with US over policy direction: defense ministry", 
   'Romania and the Republic of Korea: A strategic partnership that will grow stronger in the post-pandemic era', 
   'More than half of population expected to be over 50 in next decade', 
   'Moon urges swift measures to trace COVID-19 infections amid another wave of pandemic'], 
  ['FDI pledges to S. Korea soar 71.5% in H1 on economic recovery', 
   'Olympic baseball team to hold 1st practice on July 20', 
   'Ministry plans new building to house Lee Kun-hee collection', 
   'S. Korea to expand child care services to help more women work: minister', 
   'Pfizer vaccines under exchange deal with Israel arrive in S. Korea', 
   '37 newly enlisted soldiers at Army boot camp test positive for COVID-19', 
   '[Newsmaker] Bong Joon-ho declares Cannes festival open in Korean', 
   'Genesis launches electrified G80 sedan in S. Korea', 
   'Inseparable friends in badminton happy to be reunited in quest for medal in Tokyo', 
   'New cases most since late Dec., virus curbs extended for 1 week', 
   '[영어답게 표현하기] 영어 동사의 특성들이 잘 드러나는 문장들 2', 
   '[Graphic News] S. Korea’s global competitiveness ranking stays at 23rd in 2021: report', 
   'S. Korea records 2nd-highest daily COVID-19 cases of over 1,200', 
   'Seoul stocks open lower amid growing virus woes', 
   "Defense chief 'terribly ashamed' about one-star general's sexual abuse allegations"],
  ['Samsung expects estimate-beating Q2 earnings on robust chip biz', 
   'BTS tops Billboard Hot 100 for 6th straight week in new record', 
   'Current account surplus widens in May on robust exports', 
   'US, Chinese envoys for N. Korea hold phone talks: State Dept.', 
   '[팟캐스트] (411) 마인크래프트 19금 논란 / 이탈리아 ‘그린 패스’ 한국 미포함 ‘차별’ 논란', 
   '[Martin Schram] A 2014 memo explains our 2021 news', 
   '[Kim Seong-kon] Cultural understanding in business and diplomacy', 
   '[Editorial] Weakening posture'], [], [], [], [], []]
"""
    
    
    
    
    
    
    
    
    
