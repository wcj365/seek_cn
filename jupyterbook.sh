#!/usr/bin/bash

# Step 1. start from scratch

if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi

# Step 2. Build the static website for the book

jupyter-book build --path-output . src
mkdir docs
cp -r _build/html/* ./docs/
cp .nojekyll docs/

# Step 3. Push the changes to GitHub
git add .
git commit -m "Built the static website of the book."
git push