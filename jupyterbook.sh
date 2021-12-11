#!/usr/bin/bash

# Step 1 - Start from scratch
# Jupyter creates _build folder to store the genreated contents
# We only need to retain the html subfolder for website
# We use docs folder as the document root for setting up GitHub Pages

if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi

# Step 2 - Generate table of contents

jupyter-book toc from-project src -f jb-book -s "_*.*" src/_toc.yml


# Step 3 - Build the static website for the book
# The interim results are in _build folder

jupyter-book build --path-output . src > jupyter_book.log


# Step 4 - Push the changes to GitHub

git add .
git commit -m "Built the static website of the book."
git push
