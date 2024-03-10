#!/usr/bin/python
#-*- coding : uft-8 -*-
import os
import logRec
import cache
from natsort import natsorted
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
    words={}
    with open(rootPath + "/" + file, "r", encoding="utf-8") as file:
        cnt=0        
        temp = []
        wordClass = ""
                
        for line in file:
            lineS = line.strip()            
            if len(lineS) > 0 and lineS[0] == "-":
                wordClass = lineS[1:len(lineS)]
                continue
            if len(lineS) == 0:
                continue
            temp.append(lineS)
            if cnt % 2== 1:
                key = AddWordClass(temp[0], wordClass)
                try:
                    words[key].append(temp[1])
                except KeyError: #if a key first appeared, its list will be empty and therefore can't be appended
                    words[key] = []
                    words[key].append(temp[1])       
                temp=[]                
            cnt+=1                
        file.close()    
    return words

#SelectFile()
