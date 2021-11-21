#!/usr/bin/bash

# Step 1 Update apt-get
sudo apt-get update

# Step 2
# Install 楷体 font for Chinese Character  "AR PL UKai TW"
# https://gist.github.com/allex/11203573
sudo apt-get install fonts-arphic-ukai

# Step 3
# Install latex-cjk-all  to support Chinese/Jaopanese/Korean language for LaTex 
sudo apt install latex-cjk-all

# Step 4
# install LaTex engine (texlive) and LaTex to PDF transformation library (XeLaTex) required for Pandoc
# texlive is a LaTex engine and xetex is a Latex to PDF transformation enginer which supports UTF-8 unicode for Chinese characters
sudo apt install texlive-xetex

# Step 5
# Install Pandoc for generating PDF files
sudo apt-get install pandoc

# Step 6
# Install required Python packages for Jupyter Book for generating HTML website
pip install -r requirements.txt