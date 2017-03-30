import re
import Class
import requests as rs
from bs4 import BeautifulSoup as BS


def Login():
    pass


def Get_Merchants():
    list = []
    main_list_url = "https://www.c5game.com/dota.html"
    html = rs.get(main_list_url).content
    soup = BS(html)
    pattern = re.compile(
        '''.*?<p class="name"><a href="(.*?)"><span class=" .*? ">(.*?)</span></a></p><p class="info"><span class=".*?">Price:<span class="price">￥ (.*?)</span></span><span class="num">(.*?)piece on selling.*?''')
    for i in soup.select(".selling"):
        info = re.findall(pattern, str(i).replace("\n", ""))[0]
        list.append(Class.Merchant(info[0], info[1], info[2], info[3]))
    return list
