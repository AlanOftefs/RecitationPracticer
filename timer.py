#!/usr/bin/python
#-*- coding : uft-8 -*-
import threading
import time
import filePre
class Timer(threading.Thread):
    def __init__(self, name = None):
        threading.Thread.__init__(self, name = name)
        self.clock = 0
        self.clockPerQ = 0
    def ResetQ(self):
        self.clockPerQ = 0
    def ClearQ(self):
        self.clock -= self.clockPerQ
    def TimeFormat(self):                
        return filePre.TimeFormat(self.clock)
    def run(self):
        while True:
            time.sleep(1)
            self.clock+=1
            self.clockPerQ += 1
