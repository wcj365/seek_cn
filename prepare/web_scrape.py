#!/usr/bin/bash

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


for i in range(1, 82):

    chapter = "0" + str(i) if i < 10 else str(i)

    url = f"http://www.quanxue.cn/CT_DaoJia/LaoZi/LaoZi{chapter}.html"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page_bytes = urlopen(req).read()
    soup = BeautifulSoup(page_bytes, "html.parser")

    with open(f"../data/chapter_{chapter}.html", "w", encoding='utf-8') as f:
        f.write(str(soup))