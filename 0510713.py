# -*- coding: utf-8 -*

import requests
import time
from bs4 import BeautifulSoup
import sys

def crawl():
    url = "https://www.ptt.cc/bbs/Beauty/index.html"
    payload = {
        'from': '/bbs/Beauty/index.html',
        'yes': 'yes'
    }
    rs = requests.session()
    res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
    res = rs.get(url)
    content = res.text
    
    soup = BeautifulSoup(content, "html.parser")
    buttons = soup.find_all(class_ = 'btn wide')
    for button in buttons:
        if button.get_text().find("上頁") > -1:
            previous = button.get('href')
            break
    index = previous.find('.html')
    previous = int(previous[index-4:index])
    
    find_end = False
    while find_end is False:
        # if previous%100 == 0:
            # print(previous)
        url = "https://www.ptt.cc/bbs/Beauty/index" + str(previous) + ".html"
        
        payload = {
            'from': '/bbs/Beauty/index' + str(previous) + '.html',
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        
        soup = BeautifulSoup(content, "html.parser")
        find_date = soup.find(class_='date').get_text()
        if find_date == '12/31':
            e_index = previous
            find_end = True
        previous = previous -1
        
    find_start = False
    while find_start is False:
        # if previous%100 == 0:
            # print(previous)
        url = "https://www.ptt.cc/bbs/Beauty/index" + str(previous) + ".html"
        
        payload = {
            'from': '/bbs/Beauty/index' + str(previous) + '.html',
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        
        soup = BeautifulSoup(content, "html.parser")
        find_date = soup.find(class_='date').get_text()
        if find_date == ' 1/01':
            s_index = previous
            find_start = True
        previous = previous -1
    
    url = "https://www.ptt.cc/bbs/Beauty/index" + str(previous) + ".html"
        
    payload = {
        'from': '/bbs/Beauty/index' + str(previous) + '.html',
        'yes': 'yes'
    }
    rs = requests.session()
    res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
    res = rs.get(url)
    content = res.text
    
    soup = BeautifulSoup(content, "html.parser")
    find_date = soup.find_all(class_='date')
    
    if find_date[19].get_text() == ' 1/01':
        s_index = previous
        # print(previous)
    
    print("start index: " + str(s_index))
    print("end index: " + str(e_index))
    
    for index in range(s_index, e_index+1):
        url = "https://www.ptt.cc/bbs/Beauty/index" + str(index) + ".html"
        # print(index)
        payload = {
            'from': '/bbs/Beauty/index' + str(index) + '.html',
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        
        soup = BeautifulSoup(content, "html.parser")
        article_list = soup.find_all(class_='r-ent')
        # print(article_list)
        if index == s_index:
            for link in article_list:
                get_date = link.find_all(class_='date')
                date = get_date[0].string
                date = date.replace('/', '')
                date = date.replace(' ', '')
                if date != '101':
                    continue
                    
                get_like = link.find(class_='nrec').string
                link = link.find_all('a')
                title = link[0].string
                url_link = link[0].get('href')
                if url_link is not None:
                    url_link = "https://www.ptt.cc" + url_link
                
                if title.find("[公告]")<0 or url_link is None:
                    with open('all_articles.txt', 'a', encoding='UTF-8') as f:
                        f.write(date + ',' + title + ',' + url_link + '\n')
                    if get_like is not None and get_like == '爆':
                            with open('all_popular.txt', 'a', encoding='UTF-8') as f:
                                f.write(date + ',' + title + ',' + url_link + '\n')

        elif index == e_index:
            for link in article_list:
                get_date = link.find_all(class_='date')
                date = get_date[0].string
                date = date.replace('/', '')
                date = date.replace(' ', '')
                if date != '1231':
                    continue
                    
                get_like = link.find(class_='nrec').string
                link = link.find_all('a')
                title = link[0].string
                url_link = link[0].get('href')
                if url_link is not None:
                    url_link = "https://www.ptt.cc" + url_link
                
                if title.find("[公告]")<0 or url_link is None:
                    with open('all_articles.txt', 'a', encoding='UTF-8') as f:
                        f.write(date + ',' + title + ',' + url_link + '\n')
                    if get_like is not None and get_like == '爆':
                            with open('all_popular.txt', 'a', encoding='UTF-8') as f:
                                f.write(date + ',' + title + ',' + url_link + '\n')

        else:
            for link in article_list:
                get_date = link.find_all(class_='date')
                date = get_date[0].string
                date = date.replace('/', '')
                date = date.replace(' ', '')
                get_like = link.find(class_='nrec').string
                link = link.find_all('a')
                
                if len(link) == 0:
                    continue
                elif link[0].find('span') is not None:
                    continue
                title = link[0].string
                
                url_link = link[0].get('href')
                if url_link is not None:
                    url_link = "https://www.ptt.cc" + url_link
                if title.find("[公告]")<0 or url_link is None:
                    with open('all_articles.txt', 'a', encoding='UTF-8') as f:
                        f.write(date + ',' + title + ',' + url_link + '\n')
                    if get_like is not None and get_like == '爆':
                        with open('all_popular.txt', 'a', encoding='UTF-8') as f:
                            f.write(date + ',' + title + ',' + url_link + '\n')
                
        time.sleep(0.5)

def push(s_date, e_date):
    s_date = int(s_date)
    e_date = int(e_date)
    
    all_like = 0
    all_boo = 0
    d_like = {}
    d_boo = {}
    
    with open('all_articles.txt', 'r', encoding='UTF-8') as f:
        all_lines = f.readlines()
    for line in all_lines:
        line = line.split(',')
        if int(line[0]) < s_date or int(line[0]) > e_date:
            continue
        
        # print(int(line[0]))
        url = line[len(line)-1].replace("\n", "")
        
        payload = {
            'from': url.replace("https://www.ptt.cc", ""),
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        # print(url)
        soup = BeautifulSoup(content, "html.parser")
        comment_list = soup.find_all(class_='push')
        
        for comment in comment_list:
            comment = comment.find_all('span')
            if comment and comment[0].string == "推 ":
                all_like = all_like +1
                if comment[1].string not in d_like:
                    d_like[comment[1].string] = 1
                else:
                    d_like[comment[1].string] = d_like[comment[1].string] +1
            elif comment and comment[0].string == "噓 ":
                all_boo = all_boo +1
                if comment[1].string not in d_boo:
                    d_boo[comment[1].string] = 1
                else:
                    d_boo[comment[1].string] = d_boo[comment[1].string] +1
                       
        time.sleep(0.5)
    
    
    d_like_sort = sorted(d_like.items(), key=lambda d: d[0])
    d_like_sort = sorted(d_like_sort, key=lambda d: d[1], reverse=True)
    d_boo_sort = sorted(d_boo.items(), key=lambda d: d[0])
    d_boo_sort = sorted(d_boo_sort, key=lambda d: d[1], reverse=True)
    
    with open('push[' + str(s_date) + '-' + str(e_date) + '].txt', 'w') as f:
        f.write('all like: ' + str(all_like) + '\n')
        f.write('all boo: ' + str(all_boo) + '\n')
        for i in range(0, 10):
            f.write('like #' + str(i+1) + ': ' + d_like_sort[i][0] + ' ' + str(d_like_sort[i][1]) + '\n')
        for i in range(0, 10):
            f.write('boo #' + str(i+1) + ': ' + d_boo_sort[i][0] + ' ' + str(d_boo_sort[i][1]) + '\n')
    
def popular(s_date, e_date):
    s_date = int(s_date)
    e_date = int(e_date)
    
    count = 0
    with open('all_popular.txt', 'r', encoding='UTF-8') as f:
        all_lines = f.readlines()
    for line in all_lines:
        line = line.split(',')
        if int(line[0]) < s_date or int(line[0]) > e_date:
            continue
        count = count +1
    with open('popular[' + str(s_date) + '-' + str(e_date) + '].txt', 'w') as f:
        f.write('number of popular articles: ' + str(count) + '\n')
    
    for line in all_lines:
        line = line.split(',')
        if int(line[0]) < s_date or int(line[0]) > e_date:
            continue
        # print(int(line[0]))
        url = line[len(line)-1].replace("\n", "")
        
        payload = {
            'from': url.replace("https://www.ptt.cc", ""),
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        # print(content)
        soup = BeautifulSoup(content, "html.parser")
        link_list = soup.find_all('a')
        # print(link_list)
        for link in link_list:
            link = link.get('href')
            if link.endswith('.jpg') is False and link.endswith('.JPG') is False and \
               link.endswith('.jpeg') is False and link.endswith('.JPEG') is False and \
               link.endswith('.png') is False and link.endswith('.PNG') is False and \
               link.endswith('.gif') is False and link.endswith('.GIF') is False:
                continue
            with open('popular[' + str(s_date) + '-' + str(e_date) + '].txt', 'a') as f:
                f.write(link + '\n')
        time.sleep(0.5)
        
def keyword(keyword, s_date, e_date):
    s_date = int(s_date)
    e_date = int(e_date)
    
    with open('all_articles.txt', 'r', encoding='UTF-8') as f:
        all_lines = f.readlines()
    for line in all_lines:
        line = line.split(',')
        if int(line[0]) < s_date or int(line[0]) > e_date:
            continue
        # print(int(line[0]))
        
        url = line[len(line)-1].replace("\n", "")
        
        payload = {
            'from': url.replace("https://www.ptt.cc", ""),
            'yes': 'yes'
        }
        rs = requests.session()
        res = rs.post("https://www.ptt.cc/ask/over18", data=payload)
        res = rs.get(url)
        content = res.text
        
        soup = BeautifulSoup(content, "html.parser")
        text_all = soup.find(id='main-content')
        e_point = text_all.find_all('span', class_= 'f2')
        
        for point in e_point:
            if point.get_text().find("發信站:") > -1:
                index = str(text_all).find(str(point))
                text = str(text_all)[:(index-3)]
                break
        text = BeautifulSoup(text, "html.parser")
        text = text.get_text()
        
        if text.find(keyword) > -1:
            # print(text)
            link_list = text_all.find_all('a')
            
            for link in link_list:
                link = link.get('href')
                if link.endswith('.jpg') is False and link.endswith('.JPG') is False and \
                   link.endswith('.jpeg') is False and link.endswith('.JPEG') is False and \
                   link.endswith('.png') is False and link.endswith('.PNG') is False and \
                   link.endswith('.gif') is False and link.endswith('.GIF') is False:
                    continue
                with open('keyword(' + keyword + ')[' + str(s_date) + '-' + str(e_date) + '].txt', 'a') as f:
                    f.write(link + '\n')
        
    
if sys.argv[1] == 'crawl':
    crawl()
elif sys.argv[1] == 'push':
    push(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'popular':
    popular(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'keyword':
    keyword(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print('Invalid input!')
