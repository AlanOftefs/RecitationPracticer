#!/usr/bin/python
#-*- coding : uft-8 -*-
class ScoreCal:
    '''return a percentage'''
    def __init__(self, totalNum):
        self.totalNum=totalNum
        self.correctNum = 0
    def AddCorrect(self):
        self.correctNum+=1
    def Cal(self):
        return int(float(self.correctNum) / float(self.totalNum) * 100)
        
    
