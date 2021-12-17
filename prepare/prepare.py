#!/usr/bin/bash

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import os


for i in range(1, 82):

    chapter = "0" + str(i) if i < 10 else str(i)

    url = f"http://www.quanxue.cn/CT_DaoJia/LaoZi/LaoZi{chapter}.html"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page_bytes = urlopen(req).read()
    html = BeautifulSoup(page_bytes)


    folder = "../src/01_dao" if i <=37 else "../src/02_de"

    with open(f"{folder}/{chapter}.md", "w") as f:
        f.write("# " + chapter)
        f.write("\n\n**【经文】**\n")
        f.write(html.find("p",{"class":"jingwen"}).getText())      # 经文 
        f.write("\n**【注释】**\n") 
        f.write(html.find("p",{"class":"comment"}).getText())      # 注释
        f.write("\n**【译文】**\n")
        f.write(html.find("p",{"class":"yiwen"}).getText())      # 译文


        if html.find("div",{"class":"yinyong"}) != None:      
            f.write("\n**【引语】**\n")      
            f.write(html.find("div",{"class":"yinyong"}).getText())    # 引语

        if html.find("div",{"class":"pingxi"}) != None:
            f.write("\**【评析】**\n")
            f.write(html.find("div",{"class":"pingxi"}).getText())      # 评析

        if html.find("div",{"class":"jiedu"}) != None:
            f.write("\n**【解读】**\n")
            f.write(html.find("div",{"class":"jiedu"}).getText())      # 解读

