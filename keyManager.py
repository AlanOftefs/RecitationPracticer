#!/usr/bin/python
#-*- coding : uft-8 -*-
keyMappingAll = {}

class Key():
    def __init__(self, command, name = ""):
        self.command = command
        self.active = True
        self.name = name
    def SetActive(self, b):
        self.active = b
class KeyMapping():
    def __init__(self):
        self.keyMapping = {}
        pass
    def Add(self, key : Key):
        self.keyMapping[key.command] = key
    def BuildKeyMapping(self, command : str or chr, func, name = ""):
        if type(command) == list:
            for i in command:
                temp = Key(i, name)
                self.Add(temp)
                keyMappingAll[temp] = func
            return None
        result = Key(command, name)
        self.Add(result)
        keyMappingAll[result] = func
        return result
    def FindKey(self, command):
        return self.keyMapping[command]
    def SetActiveKey(self, command, b):
        self.FindKey(command).SetActive(b)
    def SetActiveKeys(self, command, b):
        for i in command:
            self.SetActiveKey(i, b)
    def SetActiveKeyByName(self, name, b):
        if name == "":
            raise Exception("\'name\' is empty")
            return None
        keys = list(self.keyMapping.keys())
        for i in keys:
            if self.keyMapping[i].name == name:
                self.keyMapping[i].SetActive(b)
                
    def ChangeMapping(self, command:str, func):
        self.keyMapping[self.FindKey(command)] = func
    def Invoke(self, command : str, *args):
        try:
            if self.FindKey(command).active == True:
                keyMappingAll[self.FindKey(command)](*args)
                return "R"
            else:
                return "None"
        except:
            return "None"
    def Input(self, string):
        command = input(string)
        state = self.Invoke(command)
        return (command, state)
def Test():
    keyMapping = KeyMapping()
    keyMapping.BuildKeyMapping(["A", "a"], A, "_")
    keyMapping.BuildKeyMapping("B", lambda : print("B"), "_")
    keyMapping.SetActiveKeyByName("_",False)

    while True:
        if keyMapping.Invoke(input()) == "None":
            print("No")
def A():
    print("A")
#Test()

