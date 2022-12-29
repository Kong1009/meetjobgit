# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:47:41 2022

@author: DCT
"""

# import db
import requests
from bs4 import BeautifulSoup

# cursor = db.conn.cursor()

#三立新聞

setn = "https://www.setn.com/ViewAll.aspx?PageGroupID=0&utm_source=setn.com&utm_medium=menu&utm_campaign=hotnews"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

data = requests.get(setn, headers = header).text

soup = BeautifulSoup(data, 'html.parser')

news = soup.find_all('div', class_='col-sm-12 newsItems')

for row in news:
    item = row.find('a').text
    
    h3 = row.find('h3')
    
    title = h3.text
    link = h3.find('a').get('href') #標題連結
    if not('http' in link):
        link = "https://www.setn.com" + link
    
    # print("項目：",item)
    # print("標題：",title)
    # print("連結：",link)
    # print()
    
    # sql = "select * from news where station='三立新聞' and title='{}'".format(title)
    # cursor.execute(sql)
    
    # #表示沒有資料
    # if cursor.rowcount == 0:
    #     sql = "insert into news(station, title, item, news_url) values('三立新聞', '{}', '{}', '{}')".format(title, item, link)
    #     cursor.execute(sql)
    #     db.conn.commit()
        
    
# TVBS News
tvbs = "https://news.tvbs.com.tw/realtime"

data = requests.get(tvbs, headers = header).text

soup = BeautifulSoup(data, 'html.parser')

news = soup.find('div', class_='news_list')

news = news.find('div', class_='list')

allNews = news.find_all('li')

for row in allNews:
    a = row.find('a')
    if not (a == None):
        link = row.find('a').get('href')
        if not ('http' in link):
            link = "https://news.tvbs.com.tw" + link
            
        img = row.find('img').get('data-original')
        title = row.find('h2').text
        item = row.find('div', class_='type').text
        
        print("項目：",item)
        print("標題：",title)
        print("連結：",link)
        print(img)
        print()
        
        # sql = "select * from news where station='TVBS' and title='{}'".format(title)
        # cursor.execute(sql)
        
        # #表示沒有資料
        # if cursor.rowcount == 0:
        #     sql = "insert into news(station, title, item, news_url, photo_url) values('TVBS', '{}', '{}', '{}', '{}')".format(title, item, link, img)
        #     cursor.execute(sql)
        #     db.conn.commit()
    
#華視新聞

url = "https://news.cts.com.tw/real/index.html"

data = requests.get(url, headers = header)
data.encoding = 'utf-8'
data = data.text

soup = BeautifulSoup(data, 'html.parser')

news = soup.find(id='newslist-top')

allNews = news.find_all('a')

for row in allNews:
    title = row.get('title')
    link = row.get('href')
    if not title == None:
        img = row.find('img').get('data-src')
        
        # print(title)
        # print(link)
        # print(img)
        # print()
        
        # sql = "select * from news where station='華視新聞' and title='{}'".format(title)
        # cursor.execute(sql)
        
        # #表示沒有資料
        # if cursor.rowcount == 0:
        #     sql = "insert into news(station, title, news_url, photo_url) values('華視新聞', '{}', '{}', '{}')".format(title, link, img)
        #     cursor.execute(sql)
        #     db.conn.commit()
        

# db.conn.close()
