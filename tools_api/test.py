from os import  path

file_path = path.dirname(path.abspath(__file__))
with open(file_path + r"\a.txt", "r", "utf-8") as texter:
    list = texter.readlines()