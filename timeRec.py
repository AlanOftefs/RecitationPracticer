#!/usr/bin/python
#-*- coding : uft-8 -*-
import matplotlib.pyplot as plt
import filePre

_path = "times"
_file = "times.txt"
def Add(info : tuple):
    '''(selectedFile, time), time should be measured in sec'''
    with open("%s/%s" % (_path, _file), "a+", encoding = "utf-8") as file:
        file.write(str(info[0]))
        file.write("\n")
        file.write(str(info[1]))
        file.write("\n")
        file.close()
def ShowPlot():
    fig = plt.figure(figsize = (15, 6))
    y = [] # times
    x=[]
    xLabels = []
    with open("%s/%s" % (_path, _file), "r", encoding = "utf-8") as file:
        cnt = 0
        for line in file:
            if cnt % 2 == 0:
                xLabels.append(line.strip())
            else:
                y.append(int(line.strip()))
                x.append((cnt + 1) / 2)
            cnt += 1
        file.close()
    plt.rcParams['font.family'] = 'STKAITI'
    plt.title("Times")
    plt.xticks(x, xLabels)
    plt.xlabel("Practice")
    plt.ylabel("Time Spent (s)")
    plt.grid(True)
    
    #plt.xlim(1, len(x))
    #plt.ylim(max(min(y) - 10 , 0), max(y))
    plt.bar(x, y)    
    for i in range(len(y)):        
        plt.annotate(text=y[i], xy = (x[i] +1, y[i] + 1), xytext = (x[i], y[i] + 1))
    plt.show()
#ShowPlot()


    
    
