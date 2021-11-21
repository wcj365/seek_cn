#!/usr/bin/bash

#pandoc  --metadata-file="pandoc_metadata.yml" --pdf-engine=xelatex `find ./_pandoc -name '*.md' | sort` -o peeps.pdf

pandoc --pdf-engine=xelatex `find ./_pandoc -name '*.md' | sort` -o peeps.pdf
