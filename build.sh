#!/usr/bin/bash

#1 Step 1 build static website using Jupyter Book

cd jupyter_book

. jupyterbook.sh 

# Step 2 build pdf and epub version of the book

cd pandoc

. pandoc.sh 