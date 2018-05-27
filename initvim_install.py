"""
Python script to copy init.vim file to neovim folder in home directoty
"""

import os
import shutil

HOME_DIR_PATH = os.path.expanduser('~')

source_files = os.listdir("./from/")
print(source_files)
source="./from/*"
destination="./to/"

for files in source:
  shutil.move(source, destination)
