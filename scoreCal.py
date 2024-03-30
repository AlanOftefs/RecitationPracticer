#!/usr/bin/python
#-*- coding : uft-8 -*-
from calculator import Calculator
class ScoreCal(Calculator):
    '''return a percentage'''
    def __init__(self, totalNum):
        super().__init__()
        self.totalNum = totalNum
    def Cal(self):
        return int(float(self.correctNum) / float(self.totalNum) * 100)
    def Refresh(self):
        self.correctNum = 0
        self.totalNum = 0
        
    
