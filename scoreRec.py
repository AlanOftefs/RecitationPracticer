#!/usr/bin/python
#-*- coding : uft-8 -*-
import matplotlib.pyplot as plt

_path = "scores"
_file = "scores.txt"
def Add(info : tuple):
    '''(selectedFile, score)'''
    with open("%s/%s" % (_path, _file), "a+", encoding = "utf-8") as file:
        file.write(str(info[0]))
        file.write("\n")
        file.write(str(info[1]))
        file.write("\n")
        file.close()
def ShowPlot():
    fig = plt.figure(figsize = (8, 6))
    y = [] # scores
    x=[]
    annotates = []
    with open("%s/%s" % (_path, _file), "r", encoding = "utf-8") as file:
        cnt = 0
        for line in file:
            if cnt % 2 == 0:
                annotates.append(line.strip())
            else:
                y.append(int(line.strip()))
                x.append((cnt + 1) / 2)
            cnt += 1
        file.close()
    plt.rcParams['font.family'] = 'STKAITI'
    plt.title("Scores")
    plt.xlabel("Practice No.")
    plt.ylabel("Score")
    plt.grid(True)
    
    #plt.xlim(1, len(y))
    #plt.ylim(max(min(y) - 10 , 0), 105)    
    plt.plot(x, y)
    plt.scatter(x, y, s=25, c='b')  # stroke, colour
    for i in range(len(annotates)):
        plt.annotate(text=annotates[i], xy = (x[i], y[i]), xytext = (x[i], y[i] + 1))
    plt.show()
#ShowPlot()


    
    
