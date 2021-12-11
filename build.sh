#!/usr/bin/bash

# Note: The following warning message in red from the console is ok:
# /workspaces/love/src/about.md: WARNING: document isn't included in any toctree

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


# Step 2 - Build the static website for the book
# The interim results are in _build folder

jupyter-book build --path-output . src > jupyter_book.log


# Step 3 - Copy the genreated website to docs folder 

mkdir docs
mkdir docs/offline            # to store pdf and epub version of the book
cp -r _build/html/* ./docs/   # This is the contents of the generated website
cp .nojekyll ./docs/          # required for GitHub pages to render without using jekyll


# Step 4 - Transform markdown files for PDF and epub generation

cd pandoc
python pandoc.py


# Step 5 - Generate PDF and epub files

cd ../

pandoc --pdf-engine=xelatex  `find _pandoc -name '*.md' | sort` -o docs/offline/wcj365_seek.pdf
pandoc --pdf-engine=xelatex  `find _pandoc -name '*.md' | sort` -o docs/offline/wcj365_seek.epub


# Step 6 - Push the changes to GitHub

git add .
git commit -m "Built the static website and generate pdf and epub version."
git push