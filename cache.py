#!/usr/bin/python
#-*- coding : uft-8 -*-
_path="cache"
_file="cache.txt"

class Cache:
    '''[defaultFile, score, duration]'''
    def __init__(self, _list):
        self.fields = {}
        self.fields["defaultFile"] = _list[0]
        self.fields["lastScore"] = _list[1]
        self.fields["duration"] = _list[2]
        self.keys=list(self.fields.keys())
def Write(cache):
    with open("%s/%s" %(_path, _file), "w", encoding="utf-8") as file:
        for i in cache.keys:
            file.write(cache.fields[i])
            file.write("\n")
        file.close()
def Read():    
    tempList = []
    with open("%s/%s" %(_path, _file), "r", encoding="utf-8") as file:
        for line in file:
            tempList.append(line.strip())
    result = Cache(tempList)
    return result
        
    
