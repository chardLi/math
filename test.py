from urllib import  request
from bs4 import BeautifulSoup
import re

res = request.urlopen('http://math.shu.edu.cn/CQIT2019/')
soup = BeautifulSoup(res,'html.parser')
font_div = soup.find(attrs={"id":"mainFrame"})
font_a = font_div.find_all('p')
#title = soup.find(attrs={"id":"dnn_ctr65550_ArtDetail_lblTitle"})
#print(title.text)
for font in font_a:
    print(font.decode_contents(formatter="html"))
    print('\n')
