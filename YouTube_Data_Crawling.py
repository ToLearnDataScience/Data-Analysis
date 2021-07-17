# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:40:19 2021

@author: 82108
"""

"""
Youtube_Comments_Crawling (using "Web Driver + Selenium")

- There are two types of web page. One is a "static web page" and the other is a "dynamic web page."
- To crawl data from the dynamic web page, we must use "Web Driver" & "Selenium" 
- I used "Web Driver" & "Selenium" because Youtube is one of the dynamic web pages.
  ex) Instagram, Facebook etc.
"""

'''
First Step : install web driver and import modules
- I downloaded "chromium"
- "urllib" for requesting URL.
- "bs4" for parsing data
- "selenium" for dealing with dynamic web page
   + import time 
'''

import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time


'''
Second Step : URL
- gather URL
★ I will analyze the Youtube channel "B-play" (comments about the first episode)
'''

url = "https://www.youtube.com/watch?v=MU2MyrNMves"

'''
Thrid Step : Web Driver + Selenium => BeautifulSoup(Parsing)
'''

path = "C:/Users/82108/Desktop/Study/Educational Background/Programming/개인 공부/★_Github/Data_Analysis/chromedriver_win32/"
driver = wd.Chrome(executable_path = path + "chromedriver.exe")


driver.get(url)
driver.maximize_window()
    
body = driver.find_element_by_tag_name('body')

num_of_pagedowns = 20
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    num_of_pagedowns -= 1
        
html_source = driver.page_source
    
# Parsing
html = BeautifulSoup(html_source, "lxml")
    
# extracting tag
tag = html.select('yt-formatted-string#content-text')
type(tag) # list
    
page_comments = []
for t in tag :
    cont = str(t.string)
    page_comments.append(cont)
print(page_comments)
        
driver.close()

for comment in page_comments :
    print(comment)
'''
우주야..너맞구나...? 진로찾으러 해외여행간다는애가 여기서 뭐해...어머니는 아시니?
진짜 남자 주인공 자기는 잘못 없는데 다 이해한다는듯이.... 극혐
So no one gonna say how amazing that girl was for standing up for herself cuz I’m PROUD yess that felt good . bring out THOSE FACTS guru f that jerk
어우 남친이 너무 별론데.. 자신이 잘못한걸 바로잡아주려는거를 여친이 싸우려드는걸로 몰아가버리기...
I see Chani, I watched it till the last ep. 😂 Waaah! Fantasyyyyy, anyone with me?
여주 개이쁜데 무표정일땐 ㄹㅇ 도도하게 이쁘고 웃으면 장난꾸러기같음 너무 이쁘시다 ㅜㅠ
I was so surprised when i saw Chani, i'm definetely staying
여자분 에이틴2  차아현님 아니신가요?? 앞머리없는것도 세상예쁘심
Found a new Web drama channel😍Also Chani is here.. Thankyou for the English subs
None
ㅅㅂㅋㅋㅋㅋㅋㅋㅋ와 ㅋㅋㅋㅋㅋㅋ내전남친이랑 똑같아 지가 일을 만들어놓고 싸우기 싫대 ㅋㅋㅋㅋㅋㅋ 저러면 나만 나쁜년이고 나만 속터져 죽음 진짜ㅠ
사먼의가 여주 강민아 얘기없구 우쥬뿐이네,,흑흑 민아언니 넘 예뻐ㅠㅠㅜㅜㅜ광광
That part when she kick his egg OMG i can't stop laugh so hard...😂😂😂
저남자는 왜 갑자기 끼어들어서 알까이고 없어지는거ㅋㅋㅋ
ahyun from a teen she’s more beautiful without bangs 😍
None
요리에 가장 중요한건 사랑을 담는거다 이 개자시가!!!!!
I literally shrieked when I saw CHANI
진짜 대부분의 사람들을 싸잡아 말하는건 아니지만 내가 만났던 사람들중 대부분이 저런대사를 꼭 쓰더라. 내가 불편하고 하지 않았으면 좋겠다는데 그럼 내가 너한테만 맞춰야 하냐는둥 내 인간관계가 다 끊어져야 속편하냐는둥 니가 날 조정하려한다는둥 진짜 별 말도안되는소리들.. 연애는 서로 맞춰가야하는게 연애인데 니들 멋대로 하고싶은거 다하려면 연애는 왜하는거니? 아무리 10년된 여사친이고 볼꼴 못볼꼴 다보고 지냈다고 그런 감정 1도 없다해도,  단 둘이 술먹고 늦게 들어가고 연락도 늦으면 빡치는게 당연한거고 그걸 이해못해준다고 내가 이상한 사람이 아니라 그럼 그걸 이해해주는 여자를 만나라 제발 이해할수없는 나같은 여자들한테 이해하려 강요좀 하지말고.
여자가 훨씬아까우데..
저런남자 말만ㅈㄴ잘해서 진짜 말문 막히게함ㅋㅋ말 잘하는게 진짜 잘하는게 아니라 잘하는 척하는 개소리ㅋㅋ진짜 딱 저렇게 상대방 오히려 이상한 사람으로 몰고ㅋㅋㅋ어이없어서 말이안나옴 열불나서   흥분하고 어버버 대지말고 그냥 걸러내는게 답임..
무방비로 먹다가 껍데기 씹히면 화날거같긴한데 저렇게 비꼬듯이 말하면 상대도 화날듯
when she said he's good at everything but the scene is about breaking the egg😦
None
가스라이팅 진짜 개싫어 ㅠㅠㅠㅠ
어머 would you 님이잖아..?????
None
진짜 내가 아는 쓰레기 랑 하는 거100프로 똑같다
INLOVE WITH THESE WEB SERIES !!!
여자 친구가 여자 후배를 후배로 안 보고 여자로 보인다는데 뭐가 그렇게 말이 많아 ㅋㅋㅋㅋ 그럴 거면 후배랑 사귀어야지 ;;
찬희야 ㅠㅠㅠ 진짜 드라마 나와줘서 제일 고마워 힘들텐데 연기쪽도 , 음악쪽도 모두 병행해줘서 너무 고마워 ❤️❤️ 2월달 컴백해줘서 넘 고마워 강찬희 화이팅 sf9 화이팅 😻
The main lead girl is also in a-teen she is the one with the bangs younger sister of kihyun 💖
저런 피해의식 쩌는 놈들 천지
나만남친웃을때 이빨 뿌셔버리고싶냐
I in love with her in A teen season 2. :")
쓰레기남친 역할분이 표정굳히고 초이야. 부를 때마다 씹소름,,......ㅋㅌㅋㅋㅋㅋ
None
I'm here because I want to see Chani ❤
None
우리 wouldyou 연기잘하는 비결이 머에요... ? (개아련,,,,)
남자 겁나 화나..저런 하..........진짜 짜증나는 타입 아니 화나는 거 얘기하는 게 내가 잘못한 거야? 겁나 싫어 끔찍해 하ㅋㅋㅋㅋㅋㅋㅋㅋㅋ싸우기 싫으면 언제 얘기하는데 ㅋㅋㅋㅋㅋㅋㅋㅋ
None
Chani’s role is so cute here omg I love seeing him act 💖
초이 남친 코밑에 점 나만거슬리나..
나 이거 왜 광고로 뜸..?
울우주 여기서 머하늬??? ㅋㅋㅋ 울갓찬희!! 이번작품도 대박나장
WHEN THAT RANDOM GUY STARTED PRAYING HAHA
None
I’ve liked Minah since ‘between friendship and love’ drama 😍😍😍
wait... that cute dude was sf9's chani! what a surprise, i didn't expect that at all
챤히야앙 ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ 잠깐 나와서 왜여엉?? 하는 것도 귀엽고 그냥 아니 그ㅜ이ㅕ워 아뇨도 귀여워 아 근양 사랑해 목소리 긁는 거 귀야우ㅏ 아니 섹시해 ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ 사랑스러워 귀야워 귀오궈귀여ㅜ어사망
찬희야.... 너가 너무 달달해서 내 혈관 막혀 죽겠다.....
남자가 진짜 저런다면 결혼 평생 못함 대부분 여자는, 아니지 모든 여자들이 거의 저게 정상임 나라면 여친있는 선배 저렇게 같이 있어주는 후배도 이해 안가고 싸대기 때렸음
I’m so glad that she stood up for herself instead of trying to convince herself that she was wrong.🥰❤️❤️❤️❤️
None
이따 답장하려고 놔둔거야 젼나 신박ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
None
i’m so proud of Chani 💖 MY BABYYY
ㅇㅋㅇㅋ 여주님도 남자 후배랑 술마시고 머리쓰담아주고 연락도 보고 나중에 연락하려고 보고도 답장 안할게^^ 다 널 위한거야~!! 알지?
None
강찬희 보러왔습니다 쓰앵님.
Omg so I'm freaking correct, it's kihyun sister from Ateen! OMG she looks beautiful with or without  bangs. She's kinda different without bangs. I prefer Her w/o bangs. 💕😵
여주 나인틴 (에이틴2) 차아현 아녕?
The choice of song during intense moments honestly ruins it
Continued watching because of SF9 Chani :)
None
That’s what you get when you interfere with lovers quarrel 😂
우주,우주하는데 찬희에요 여러분...강찬희라고요!!
lol i love it it's just the first ep and they were fighting
i dont think breaking an egg makes you good at everything..
여주 그....사당보다 먼 의정부보단 가까운...여기에 나왔던가?
9~10분쯤 보며느낀건데 카메라 화면 너무 움직이는것같아요ㅠㅠ
서로노력하고 바뀌다바뀌다 안되서 안맞아서 헤어지는건 솔직히 서로 어쩔수없고 이해가는이별이지만 다른건 존나 왜그럴꺼면서 연애를하는지..
None
None
강찬희 너무 귀엽다 최고다 짜릿해 ❤
Teaching how to crack eggs open ? Really ? Like who can't do that ...
여주 개시원하다 앞으로 애청할게요 👍🏻
강차늬 ㅜㅜㅜㅜㅜㅜ
Omg, girl you're so pretty, just find another man who deserves you. The heck is with that guy.
찬희가 왜 요기서 나오늬 엄훠 우주야
아현이 ㅠ 에이틴 아혀니 💗🤗 넘무 이뻐 ㅠ 🥰
찬희야! 우리 스카이캐슬 우주! 꺄아아아
she's so different without bangs. why the heck she so pretty. i can't
None
어휴 저남자 개쓰레기다 초이 사이다 사랑해 ❤️❤️❤️❤️
헐 여주왤케 낯있나했더니 ㅇㅇㅌ 차아현님..
What is the food called? It looks delicious
Omg the first episode is so hilarious I'm going to watch it 😂 😂 😂
None
근데 이와중에 여주 넘나 예쁘다.
Ohmyygaad why would he go between them?! 😂😂
None
None
차니 눈 똥글~해지는거 너무 귀엽다ㅠㅠㅠㅠㅜㅜㅜㅜㅜㅠ
None
OMG chani is sooo cute ❤️❤️❤️❤️😍
Accidentally came across this drama and found chani, now im excited
우주오빠 ㅠㅠㅠ♥♥
Let this be a bl 🙏😂
None
I see some bromance at the end
Ok no that smile has me dead 💀🤩🔥🤪💫🥰🥰
오와 여주분 박하영에 나오신 서브여주시네 ㄷㄷ 여전히 연기 잘하신당 ㄷㄷ
I clicked then I saw Chani... Wowww gonna watch till the last ep evsnthough I'm having an exam... ㅋㅋㅋㅋ
우주 여행 중에 딴 길로 샜군
ㄹㅇ 에그 인 헬ㄹ이넼ㅋㅅㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅌㅋㅋㅋㅋㅋㅋㅋㅋ
달걀 저거 깨는거 누가 몰랔ㅋㅋㅋㅋㅋㅋㅋ
Ahhyun's hair is so flawless... lol
8:55
민아 언니 사랑해요 개이뻐 연기도 너무잘해 천재야 ㅠㅠㅠㅠㅠㅠㅠㅠ
하... 강찬희 잘생겼어 ㅠㅠㅠㅠㅠㅠ
YAAAS LEZZGO GIRL ❤️🤘
헐 여주 헐 여주가 헐 민아언니ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 근데 찬희도 있어ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ😭😭
앜ㅋ 마지막ㅋㅋㅋ
목소리는 안 높이는데 좀 재수없게(?) 말하는 스타일이네
누가 이렇게 찬희가 유명해질줄 알았겠어..ㅎ
저 여자분 에이틴에 나오는 아현이 느낌 나는듯..? 아닌듯.. 맞나? 맞죠??????? 🤭🤭🤭
뭐..? 강찬희요..??!?!??!? 강찬희요ㅠㅠㅠ???????
남주는 뭐가 저렇게 당당해서..
저런 스탈은 그냥 안만나는게 답이더라ㅋㅋ 저런 스탈은 헤어질때도 지가 잘나서 헤어짐ㅎㅎ자기 잘못은 하나도 없더라ㅎㅎ내 자존감만 낮아지는거지ㅎㅎ항상 내 잘못이 되는거니까ㅎㅎ저런 머저리들은 차면 된다:) 내 전남친한테 마지막 여주 대사 해주고 싶넹ㅎㅎ속이 후련함
That Girl named Choi is beautiful in every angle😌
None
Ah hyun and Uju is here!! 😍
찬희 잘생겼닼ㅋㅋ
와 여주 진짜 속시원하게 말하는거 너무 좋다 앞으로 애청할구양😚
헐....찬희오빠다....ㅠㅠㅠㅠㅠㅠㅠ완전 잘생겼어!♥♥♥찬희오빠 연기잘한다><멋있어😍마지막에 손잡아주고 괜찮냐고 물어보는거 겁나착하당
None
강민아ㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜㅜ 사랑해ㅜㅜㅜㅜㅜㅜㅜㅜ
아무거나 찍어서 봤는데 찬희 오빠자낭 ㅜㅜㅜ
찬희 존잘... 이거만 기다렸어ㅠㅠ
So perfect!
실제로   저러시면    데이트폭행  크게다치면    상해치사로  처벌받습니다
ㅋㅋㅋㅋㅋ마지막 남자ㅂ랄 어쩔거야
What if he's still meeting just one of his friend! I mean harry and hermoine were even more intimate but they were just frnds y"ll know right?
The painnnn 😂😂😭😭😭
cha ahyun look more cute if she put her bangs 😍❤️ i’m not saying that she’s ugly without bangs she look pretty without bangs and cute with bangs 😍❤️
민아 이뿌다ㅜㅠㅠㅠㅠ아ㅠㅠㅠㅠㅠㅠ
민아님 개이쁘다 진짜ㅠㅠㅠㅠㅠ 찬희님 사랑해요
뭐가 저게 완벽한 놈이야 ㅅㅂㅋㅋㅋ 여주도 참 보는눈이 없다....
'''




















