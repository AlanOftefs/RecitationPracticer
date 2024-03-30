#!/usr/bin/python
#-*- coding : uft-8 -*-
import sys
import random
import os
import cache as cac
import logRec
import filePre
import scoreRec
import timeRec
import resourceManager
import mistakeRec
import globalManager as GM
from ask import Ask
import enterDebugMode

def OnRest():
    print(len(GM.qs))
    GM.timer.ClearQ()
def OnShowans():
    print(GM.qs[0].anses)
    if GM.wrongCntDown > 0:
        mistake = mistakeRec.Mistake(GM.selectedFile, GM.qs[0])
        mistakeRec.Add(mistake)
    Next()
def OnReturn():
    global goRe
    print("\n")            
    goRe = True
def OnScore():
    scoreRec.ShowPlot()
def OnTime():
    timeRec.ShowPlot()
'''
def OnClear():
    global resourceManager
    resourceManager.Clear()
'''
def ShowMistakesFolder():
    os.startfile("mistakes")

GM.keyMapping.BuildKeyMapping("rest", OnRest, "1")
GM.keyMapping.BuildKeyMapping("showans", OnShowans, "1")
GM.keyMapping.BuildKeyMapping(["R", "r", "ｒ"], OnReturn, "2")
GM.keyMapping.BuildKeyMapping(["S", "s", "ｓ"], OnScore, "2")
GM.keyMapping.BuildKeyMapping(["T", "t", "ｔ"], OnTime, "2")
GM.keyMapping.BuildKeyMapping(["M", "m", "ｍ"], ShowMistakesFolder, "2")
#GM.keyMapping.BuildKeyMapping(["C", "c", "ｃ"], OnClear, "2")

while True:
    GM.selectedFile = filePre.SelectFile()

    words=filePre.Read(GM.selectedFile)
    try:
        qsNum = int(input("%s questions in all, how many do you want to practice?All by default.\n"
                          % str(len(words))))
    except:
        qsNum = len(words)
        print("Unexpected response. All will be practices")
    finally:
        print("%d out of %d selected" % (qsNum, len(words)))
    
    print("--------------------------------")
    GM.scoreCal.totalNum = qsNum

    for i in range(len(words) ** 2):
        random.shuffle(words)
    GM.qs = words[0 : qsNum]

    print("Type \"showans\" to jump and get answer")
    def Next():
        GM.qs.pop(0)
        GM.wrongCntDown = 2
        GM.timer.ResetQ()

    GM.timer.start()

    GM.keyMapping.SetActiveKeyByName("2", False)
    GM.keyMapping.SetActiveKeyByName("1", True)
    ask = Ask()
    #ask
    ask.Run()

    print("--------------------------------")
    print("All Has Been Done. You got %d%s." % (GM.scoreCal.Cal(), '%'))
    print("Total Time Spent: %s" % GM.timer.TimeFormat())
    print("Time Spent Per Q: %s" % filePre.TimeFormat(GM.timer.clock / qsNum))

    #cache operations
    try:
        if GM.selectedFile != "test.txt":
            #scoreRec.Add((selectedFile , GM.scoreCal.Cal()))
            #timeRec.Add((selectedFile, timer.clock)) # calculate average time spent
            mistakeRec.Record()
            mistakeRec.Clear()
            argsList = [str(GM.selectedFile), str(GM.scoreCal.Cal()), str(GM.timer.clock)]
            cacheSample=cac.Cache(argsList)
            cac.Write(cacheSample)
        print("Cache successfully saved!")
        
    except BaseException as exc:
        logRec.Log.RecordExc(exc)
        print("Cache failed to save! Check log/log.txt")
    finally:
        print("Type [R] to practise another.")
        print("Type [S] to view your SCORE plot")
        print("Type [T] to view your TIME bar")
        print("Type [M] to view your mistakes recorder")
        #print("Type [C] to CLEAR your score and time data")
        print("Type [Any] to exit")

    GM.keyMapping.SetActiveKeyByName("1", False)
    GM.keyMapping.SetActiveKeyByName("2", True)

    goRe = False
    while goRe == False:
        command = input()
        state = GM.keyMapping.Invoke(command)
        if state == "None":
            sys.exit()
