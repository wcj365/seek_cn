import os
import shutil
from glob import glob

TARGET_FOLDER = "_pandoc"

if os.path.exists(TARGET_FOLDER):
    shutil.rmtree(TARGET_FOLDER)

os.mkdir(TARGET_FOLDER)

shutil.copyfile("src/_pandoc.md", TARGET_FOLDER + "/00_title_toc.md")

source_folders = glob("src/*/")

for folder in source_folders:
    files = glob(folder + "*.md")
    files.sort()
    if not folder + "00.md" in files:
        continue
    chapter_file = TARGET_FOLDER + "/"+ folder.split("/")[2] + ".md"
    if os.path.exists(chapter_file):
        os.remove(chapter_file)
    with open(chapter_file, "a") as f_append:
        with open(folder + "00.md", "r") as f_read:
            f_append.write(f_read.readline())
            f_append.write("\n")
        for file in files:
            if "00.md" in file:
                continue
            with open(file, "r") as f_read:
                f_append.write("#")
                lines = f_read.readlines()
                for line in lines:
                    if "![]" in line:
                        f_append.write("![](" + "../" + folder + "/" + line[4:])
                    else:
                        f_append.write(line)
                f_append.write("\n\n")
                f_append.write("\\newpage")
                f_append.write("\n\n")
 