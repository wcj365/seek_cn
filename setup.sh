#!/usr/bin/bash

# Step 1
# Install required Python packages

pip install -r requirements.txt

sudo apt-get update

# Step 2 
# Install 楷体 font for Chinese Character
# https://gist.github.com/allex/11203573

sudo apt-get install fonts-arphic-ukai

# Step 3
# Install pandoc

sudo apt-get install pandoc
