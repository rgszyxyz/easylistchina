import os

with open("easylistchina.txt",encoding='utf-8') as file:
    for f in file:
        if f[:2]=="||":
            print (f[:2])
            domain=f.split("^")[0][2:]
            print (domain)


