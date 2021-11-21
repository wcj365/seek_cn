#!/usr/bin/bash

#pandoc  --metadata-file="pandoc_metadata.yml" --pdf-engine=xelatex `find ./_pandoc -name '*.md' | sort` -o peeps.pdf

pandoc --pdf-engine=xelatex `find ./_pandoc -name '*.md' | sort` -o ./pdf/peeps.pdf

# Push the changes to GitHub
git add .
git commit -m "Built the PDF verion of the book."
git push