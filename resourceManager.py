#!/usr/bin/python
#-*- coding : uft-8 -*-
_sPath = "scores"
_sFile = "scores.txt"
_tPath = "times"
_tFile = "times.txt"
_qPath = "qs"

def Clear():
    '''(selectedFile, time), time should be measured in sec'''
    with open("%s/%s" % (_sPath, _sFile), "w", encoding = "utf-8") as file:
        file.write("")
        file.close()
    with open("%s/%s" % (_tPath, _tFile), "w", encoding = "utf-8") as file:
        file.write("")
        file.close()
def AddQ(name, qsDict):
    keys = list(qsDict.keys())
    with open("%s/%s" % (_qPath, name), "w", encoding = "utf-8") as file:
        for i in keys:
            file.write(i)
            file.write("\n")
            file.write(qsDict[i])
            file.write("\n")
        file.close()
    


    
    
