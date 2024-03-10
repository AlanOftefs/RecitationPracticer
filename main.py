#!/usr/bin/python
#-*- coding : uft-8 -*-
import sys
import random
import os
import cache as cac
import scoreCal as sc
import logRec
import filePre
import timer as ti
import scoreRec
import timeRec
import resourceManager
import keyManager
import mistakeRec

def OnRest():
    global keys
    global timer
    print(len(keys))
    timer.ClearQ()
def OnShowans():
    print(words[keys[0]])
    global wrongCntDown
    if wrongCntDown > 0:
        mistake = mistakeRec.Mistake(selectedFile, keys[0])
        mistakeRec.Add(mistake)
    Next()
def OnReturn():
    global goRe
    print("\n")            
    goRe = True
def OnScore():
    global scoreRec    
    scoreRec.ShowPlot()
def OnTime():    
    global timeRec    
    timeRec.ShowPlot()
def OnClear():
    global resourceManager
    resourceManager.Clear()
    
keyMapping = keyManager.KeyMapping()
keyMapping.BuildKeyMapping("rest", OnRest, "1")
keyMapping.BuildKeyMapping("showans", OnShowans, "1")
keyMapping.BuildKeyMapping(["R", "r", "ｒ"], OnReturn, "2")
keyMapping.BuildKeyMapping(["S", "s", "ｓ"], OnScore, "2")
keyMapping.BuildKeyMapping(["T", "t", "ｔ"], OnTime, "2")
#keyMapping.BuildKeyMapping(["C", "c", "ｃ"], OnClear, "2")

while True:
    selectedFile = filePre.SelectFile()

    words=filePre.Read(selectedFile)
    try:
        qsNum = int(input("%s questions in all, how many do you want to practice?All by default.\n"
                          % str(len(words))))
    except:
        qsNum = len(words)
        print("Unexpected response. All will be practices")
    finally:
        print("%d out of %d selected" % (qsNum, len(words)))
    
    print("--------------------------------")
    keys=list(words.keys())
    scoreCal = sc.ScoreCal(qsNum)

    for i in range(len(words) ** 2):
        random.shuffle(keys)
    keys = keys[0 : qsNum]

    print("Type \"showans\" to jump and get answer")
    wrongCntDown = 2
    def Next():
        global keys,wrongCntDown
        keys.pop(0)
        wrongCntDown = 2
        timer.ResetQ()

    timer = ti.Timer()
    timer.start()

    keyMapping.SetActiveKeyByName("2", False)
    keyMapping.SetActiveKeyByName("1", True)    
    #main
    while len(keys) > 0:
        ans=input(keys[0] +  " : ")
        state = keyMapping.Invoke(ans)       
        if state == "None":
            if ans not in words[keys[0]]:
                wrongCntDown -= 1
                if wrongCntDown > 0:
                    print("Wrong, %d chances left" % wrongCntDown)
                else:                    
                    print("You won't get this score")
                    if wrongCntDown == 0:
                        mistake = mistakeRec.Mistake(selectedFile, keys[0])
                        mistakeRec.Add(mistake)
            else:        
                if wrongCntDown > 0:
                    scoreCal.AddCorrect()
                Next()
    print("--------------------------------")
    print("All Has Been Done. You got %d%s." % (scoreCal.Cal(), '%'))
    print("Total Time Spent: %s" % timer.TimeFormat())
    print("Time Spent Per Q: %s" % filePre.TimeFormat(timer.clock / qsNum))  

    #cache operations
    try:
        if selectedFile != "test.txt":
            #scoreRec.Add((selectedFile , scoreCal.Cal()))
            #timeRec.Add((selectedFile, timer.clock)) # calculate average time spent
            mistakeRec.Record()
            mistakeRec.Clear()
            argsList = [str(selectedFile), str(scoreCal.Cal()), str(timer.clock)]            
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
        #print("Type [C] to CLEAR your score and time data")
        print("Type [Any] to exit")

    keyMapping.SetActiveKeyByName("1", False)
    keyMapping.SetActiveKeyByName("2", True)

    
    command = ""
    goRe = False
    while goRe == False:
        command = input()
        state = keyMapping.Invoke(command)
        if state == "None":
            sys.exit()
