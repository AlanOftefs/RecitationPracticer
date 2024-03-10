#!/usr/bin/python
#-*- coding : uft-8 -*-
import resourceManager
_path = "mistakes"
_file = "mistakes.txt"
class Mistake:
    def __init__(self, practice = "", subject = "", ans = ""):
        self.practice = practice
        self.subject = subject
        self.ans = ans
mistakes = []
def Add(mistake):
    mistakes.append(mistake)
def Clear():
    mistakes.clear()
def Read():
    result = []
    cnt = 0    
    with open("%s/%s" % (_path, _file), "r", encoding = "utf-8") as file:
        for line in file:
            lineS = line.strip()
            if cnt % 3 == 0:
                mistake = Mistake()
                mistake.practice = lineS
            elif cnt % 3 == 1:            
                mistake.subject = lineS                
            else:
                mistake.ans = lineS
                result.append(mistake)
            cnt += 1
        file.close()
    return result
            
def Record():
    with open("%s/%s" % (_path, _file), "a+", encoding = "utf-8") as file:
        for mistake in mistakes:
            file.write(mistake.practice)
            file.write("\n")
            file.write(mistake.subject)
            file.write("\n\n")
        file.close()
def GenerateQ():
    temp = Read()
    mistakeDict = {}        
    for mistake in temp:
        mistakeDict[mistake.subject] = mistake.ans
    resourceManager.AddQ("mistakes.txt", mistakeDict)
GenerateQ()
