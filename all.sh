#!/usr/bin/bash

# Step 1. Build the web site version of the book
. jupyterbook.sh

# Step 2. Build the PDF version of the book
. pandoc.sh