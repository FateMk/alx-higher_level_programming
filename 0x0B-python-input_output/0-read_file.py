#!/usr/bin/python3
def read_file(filename=""):
    with  open(filename, mode='w', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
