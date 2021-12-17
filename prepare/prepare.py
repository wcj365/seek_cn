#!/usr/bin/bash

import requests
from bs4 import BeautifulSoup

url = "http://www.quanxue.cn/CT_DaoJia/LaoZi/LaoZi01.html"
import os
import cn2an


for i in range(1, 82):

    chapter = "0" + str(i) if i < 10 else str(i)

    url = f"http://www.quanxue.cn/CT_DaoJia/LaoZi/LaoZi{chapter}.html"

    git 

def transform(part):

    # Step 1 - Read the source data

    with open(part + ".mhtml", "r") as f:
        lines = f.readlines()

    # Step 2 - Create 00.md 
    
    with open(f"../src/{part}/00.md", "w") as f:
        f.write("# ")
        f.write(lines[0])
        f.write("\n")
        f.write("```{tableofcontents}")
        f.write("\n")
        f.write("```")

    # Step 3 - Create mapping for each chapter (chapter number and starting line number)

    articles = []
    for index, line in enumerate(lines):
        if "、" in line:   
            cn = line.split("、")[0]
            try:
                an = cn2an.cn2an(cn) 
                articles.append((cn, an, index)) 
            except:
                continue

    # Step 4 - Create article files

    for index, article in enumerate(articles):
        an = article[1]
        if an < 10:
            an = "0" + str(an)
        else:
            an = str(an)

        with open(f"../src/{part}/{an}.md", "w") as f:
            f.write("# ")
            if index + 1 == len(articles):
                f.writelines(lines[article[2]:])  
            else:        
                f.writelines(lines[article[2]:articles[index + 1][2]])
      

parts = ["02_shang_pian", "03_zhong_pian", "04_xia_pian"]

for part in parts:
    
    folder = "../src/" + part
    if not os.path.isdir(folder):
        os.mkdir(folder)
    transform(part)