import os
import re

with open("easylistchina.txt",encoding='utf-8') as file:
    for f in file:
        if f[:2]=="||":
            domain=f.split("^")[0][2:]
            if domain.find("*")<0 and domain.find("@")<0 and domain.find("/")<0 and domain.find("=")<0 and domain.find("$")<0:
                print ("0.0.0.0 " + domain)


