#!/usr/bin/bash

# Step 1. Transform the contents for Pandoc

python pandoc.py

# Step 2. Generate PDF version of the book

pandoc --pdf-engine=xelatex `find ./_pandoc -name '*.md' | sort` -o ./pdf/peeps.pdf

# Step 3. Push the changes to GitHub

git add .
git commit -m "Built the PDF verion of the book."
git push