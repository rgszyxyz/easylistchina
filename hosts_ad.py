import os
import re

with open("easylistchina.txt",encoding='utf-8') as file:
    for f in file:
        #if f[:2]=="||":
        if re.match("^\|\|.*\^",f):
            #print (f)
            domain=f.split("^")[0][2:]
            #print (domain)
            if f.split("^")[1].find('\n')==0 or f.split("^")[1].find('$third-party')==0:
            #if domain.find("third-party")>0 and domain.find("@")<0 and domain.find("/")<0 and domain.find("=")<0 and domain.find("$")<0:
                print ("0.0.0.0 " + domain, "\t"+f, end='')


