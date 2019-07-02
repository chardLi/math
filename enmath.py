from urllib import request
from bs4 import BeautifulSoup
import re

def content(string):
    res = request.urlopen('http://en.math.shu.edu.cn/')
    soup = BeautifulSoup(res, 'html.parser')
    ListUrls = soup.find_all('a',href=re.compile(string))
    return ListUrls

def printadd(ListUrls):
    for url in ListUrls:
        print(url.string)
        if url.get('href').startswith('http'):
            print(url.get('href'))
        else:
            print('http://en.math.shu.edu.cn' + url.get('href'))

if __name__=='__main__':
    ListUrls1 = content('\/Default.aspx\?tabid=35096&ctl=Detail&mid=65550&Id=[230602,239979].*')
    printadd(ListUrls1)

    ListUrls2 = content('\/LinkClick.aspx\?link=.*')
    printadd(ListUrls2)