import requests as rt
from bs4 import BeautifulSoup
import urllib
import os 
import time
import numpy as np
import re

#start_url = '  '
page = 1
ini_url = 'https://www.thesun.co.uk/'
start_url = 'https://www.thesun.co.uk/page/'+ str(page)+ '/?'
param = {
    #ohttps://www.thesun.co.uk/page/3/?s=China
    's' : 'China'
}
#param['searchPhrase'] = 'Xi+Jinping+common+destiny'
#param['s'] = 'community of common destiny'
#param['s'] = 'community with a shared future'
param['s'] = 'Xi Jinping'
#param['offset'] = 0
url = start_url + urllib.parse.urlencode(param)
print(url)
data = rt.get(url)
content = data.content
soup = BeautifulSoup(content,'lxml')
a = soup.find(class_ = 'search-result-count').text.split()[0]
a = re.findall(r"\d+\.?\d*",a)
b = str()
for i in range(len(a)):
    b = b + a[i]
sum = int(b)
sum1 = sum
count = 0
each_url = []
#offset = 0
#sum = 50
address = 'txt_file_Xi/'
while count < sum/10:
    if count != 0:
        #param['offset'] += 50
        page = page + 1
        start_url = 'https://www.thesun.co.uk/page/'+ str(page)+ '/?'
        url = start_url + urllib.parse.urlencode(param)
        #print(url)
        data = rt.get(url)
        soup = BeautifulSoup(data.content,'lxml')
    d = soup.find_all(class_ = 'teaser-anchor teaser-anchor--search')
    for i in range(10):
        '''ran = []
        ran.append(np.random.randint(0,6))
        ran.append(np.random.randint(6,10))'''
        #print(ini_url + d[i]['href'])
        temp_url = ini_url + d[i]['href']
        each_url.append(temp_url)
        temp_get = rt.get(temp_url)
        soup1 = BeautifulSoup(temp_get.content,'lxml')
        Text = {
            'Title':'None',
            'Url':'None',
            'Time':'None',
            'Text':'None'
        }
        try:
            Text['Title'] = soup1.find(class_ = 'article__headline').string
        except BaseException:
            pass

        try:
            Text['Url'] = ini_url + d[i]['href']
        except BaseException:
            pass

        try:
            Text['Time'] = soup1.find(class_ = 'article__published').text
        except BaseException:
            pass

        try:
            Text['Text'] = soup1.find(class_ = 'article__content').text
        except BaseException:
            pass

        '''Text = {
            'Title':soup1.h2.string,
            'Url':ini_url + d[count*50+i]['href'],
            'Time':soup1.find(class_ = 'article-timestamp-label').next_sibling.string,
            'Text':soup1.find(itemprop = 'articleBody').text
        }'''
        print("\n\nCount:",count*10+i+1)
        print(Text['Title'],'\n')
        file_name = address + str(count*10+i+1) + '.txt'
        try:
            with open(file_name,'w') as f:
                for i in Text:
                    f.write(Text[i]+'\n')
        except:
            pass
        #time.sleep(0.1)
    count = count+1
#print(each_url)
print('一共有：',sum1,'\n')
#print(soup.prettify())


'''
rt.get(ini_url + d[i]['href'])
soup1 = BeautifulSoup(d1.content,'lxml')
Text = {
    'Title':soup1.h2.string,
    'Url':ini_url + d[0]['href'],
    'Time':soup1.find(class_ = 'article-timestamp-label').next_sibling.string,
    'Text':soup1.find(itemprop = 'articleBody').text
}'''
#print('Title:',soup1.h2.string)
#print('Url:',ini_url + d[0]['href'])
#print('Time:',soup1.find(class_ = 'article-timestamp-label').next_sibling.string)
#print('Text:',soup1.find(itemprop = 'articleBody').text)
#print(soup1.p.next_sibling.string)
#print(Text)