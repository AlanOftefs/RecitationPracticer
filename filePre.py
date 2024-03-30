#!/usr/bin/python
#-*- coding : uft-8 -*-
import os
import logRec
import cache
from natsort import natsorted
from question import Question, PassingMode
from specialChrDetector import SpecialChrDetector
rootPath="qs"

def TimeFormat(oSec):        
        hour = 0
        minute = 0
        second = oSec % 60
        if oSec >= 60:
            minute += oSec // 60            
        if minute >= 60:
            hour += minute // 60
            minute %= 60
        result = "%02dh : %02dm : %02ds" % (hour, minute, second)
        return result
    
def SelectFile():    
    files=os.listdir(rootPath)
    files = natsorted(files)
    
    for i in range(len(files)):
        print("%s. %s" % (i, files[i]))
        
    try:
        print("Last time you practice %s, %s%s scored, %s spent, %s having been selected by default."
          %(cache.Read().fields["defaultFile"],
            cache.Read().fields["lastScore"],
            '%',
            TimeFormat(int(cache.Read().fields["duration"])),
            cache.Read().fields["defaultFile"]))
    except:
        print("It's your first time to use...")
        logRec.Log.RecordStr("Detected none in cache/cache.txt")
    print("-------------------------")
    result = input("Which to practise: ")
    if result.strip() == "":
        selectedFile = cache.Read().fields["defaultFile"]
    try:
        selectedFile = files[int(result)]
    except Exception as exc:
        selectedFile = cache.Read().fields["defaultFile"]
        logRec.Log.RecordExc(exc)
        print("Failed to select practice! %s selected by default! Check log/log.txt" % cache.Read().fields["defaultFile"])        
    return selectedFile

def AddWordClass(word, wordClass):
    if wordClass != "":
        return "%s %s." % (word, wordClass)
    else:
        return word
def Read(file):
    words=[]
    cnt = 0
    wordClass = ""
    with open(rootPath + "/" + file, "r", encoding="utf-8") as file:
        for line in file:
            lineS = line.strip()
            if len(lineS) == 0:
                continue
            #Filter the line with special characters
            scd = SpecialChrDetector(lineS)
            if scd.GetType() == "WordClass":
                wordClass = lineS[1:len(lineS)]
            elif scd.GetType() == "Repeating":
                if len(words) == 0 or words[-1].passingMode != PassingMode.all or words[-1].GetContent() != lineS:
                    temp = Question(lineS, [], wordClass, PassingMode.all)
                    words.append(temp)
                cnt += 1
            elif scd.GetType() == "None": #question or ans
                if cnt % 2 == 0: #Normal question being received
                    if len(words) == 0 or words[-1].GetContent() != lineS:
                        temp = Question(lineS, [], wordClass, PassingMode.any)
                        words.append(temp)
                elif cnt % 2 == 1: # All ansed
                    words[-1].AddAns(lineS)
                cnt += 1
        file.close()    
    return words

#SelectFile()
if __name__ == "__main__":
    test = Read("38毛皮.txt")
    for i in test:
        if "候補地" in i.anses:
            print(i.Check("候補地"))
