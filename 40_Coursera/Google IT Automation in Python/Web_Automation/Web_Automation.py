#!/usr/bin/env python3

import os
import requests


def get_files(path):
    files = []
    files_dict = []
    keys = ["title", "name", "date", "feedback"]
    for archivo in os.scandir(path):
        if archivo.name.endswith(".txt"):
            files.append(os.path.join(path, archivo.name))
        else:
            continue

# ------ Debug Lines ------
#   print(files)
# ------ Debug Lines ------
    for file in files:
        with open(file, mode='r') as f:
            text = f.read().splitlines()
        files_dict.append(dict(zip(keys, text)))
# ------ Debug Lines ------
#   print(files_dict)
# ------ Debug Lines ------
    return files_dict


def post_web(web, files_dict):
    response = requests.post(web, data = files_dict)
    return None


def main():
    path = r'/home/techno1731/Documents/00_DS-Roadmap/40_Coursera/Google IT Automation in Python/Web_Automation'
    files_dict = get_files(path)
    print(files_dict)
    return None


if __name__ == "__main__":
    main()
