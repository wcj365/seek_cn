#!/usr/bin/bash

# Step 1
# Install required Python packages for Jupyter Book
pip install -r requirements.txt

# Step 2 Update apt-get
sudo apt-get update

# Step 3 
# Install 楷体 font for Chinese Character  "AR PL UKai TW"
# https://gist.github.com/allex/11203573
sudo apt-get install fonts-arphic-ukai

# Step 4
# Install latex-cjk-all  to support Chinese/Jaopanese/Korean language for LaTex 
sudo apt install latex-cjk-all`


# Step 5
# install LaTex engine (texlive) and LaTex to PDF transformation library (XeLaTex) required for Pandoc
# texlive is a LaTex engine and xetex is a Latex to PDF transformation enginer which supports UTF-8 unicode for Chinese characters
sudo apt install texlive-xetex

# Step 6
# Install pandoc
sudo apt-get install pandoc
