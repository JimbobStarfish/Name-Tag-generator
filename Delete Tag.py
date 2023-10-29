import os

path = "tag.txt"

try:
    os.remove(path)
    os.rmdir(path)
except FileNotFoundError:
    print("you sadly can not delete because the file has not been found")