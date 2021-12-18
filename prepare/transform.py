#!/usr/bin/bash

from bs4 import BeautifulSoup

for i in range(1, 82):

    chapter = "0" + str(i) if i < 10 else str(i) 
    
    file = f"../data/chapter_{chapter}.html"

    html = BeautifulSoup(open(file, encoding="utf8"), "html.parser")

    folder = "../src/01_dao" if i <=37 else "../src/02_de"

    with open(f"{folder}/{chapter}.md", "w") as f:
        f.write("# 第 " + chapter + " 章")
        f.write("\n")
        f.write(html.find("p",{"class":"jingwen"}).getText())      # 经文 
        f.write("\n**【注释】**\n\n") 
        f.write("- " + "\n- ".join(html.find("p",{"class":"comment"}).getText().strip().strip("\n").split("\n")))      # 注释 
        f.write("\n\n**【译文】**\n")
        f.write(html.find("p",{"class":"yiwen"}).getText())      # 译文


        if html.find("div",{"class":"yinyong"}) != None:      
            f.write("\n**【引语】**\n")      
            f.write(html.find("div",{"class":"yinyong"}).getText())    # 引语

        if html.find("div",{"class":"pingxi"}) != None:
            f.write("\n**【评析】**\n")
            f.write(html.find("div",{"class":"pingxi"}).getText())      # 评析

        if html.find("div",{"class":"jiedu"}) != None:
            f.write("\n**【解读】**\n")
            f.write(html.find("div",{"class":"jiedu"}).getText())      # 解读

