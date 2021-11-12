import requests
from bs4 import BeautifulSoup
from jieba.analyse import extract_tags

url = 'https://www.ptt.cc/bbs/sex/M.1636564376.A.D5F.html'
ans = requests.get(url, cookies={'over18':'1'})
response = BeautifulSoup(ans.text)

main = response.find('div', id='main-content')
meta = main.find_all('span', class_='article-meta-value')
print('作者:',meta[0].text)
print('看板:',meta[1].text)
print('標題:',meta[2].text)
print('時間:',meta[3].text)

a = main.find_all('div', class_='article-metaline')
for i in a:
    i.extract()
b = main.find('div', class_='article-metaline-right')
b.extract()

push = main.find_all('span', class_='push-tag')
total = 0
for x in push:
    if '推' in x.text:
        total += 1
    elif '噓' in x.text:
        total -= 1

c = main.find_all('div', class_='push')
for a in c:
    a.extract()

p = main.find_all('span', class_='f2')
for x in p:
    x.extract()

print('總分:',total)
print('本文:',main.text)
print('關鍵字:', extract_tags(main.text, 10))