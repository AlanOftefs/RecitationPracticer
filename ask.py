import globalManager as GM
import mistakeRec
from question import *

class KeyMethods:
    @staticmethod
    def OnRest():
        print(len(GM.qs))
        GM.timer.ClearQ()
    @staticmethod
    def OnShowans():
        print(GM.qs[0].anses)
        if GM.wrongCntDown > 0:
            mistake = mistakeRec.Mistake(GM.selectedFile, GM.qs[0])
            mistakeRec.Add(mistake)
        GM.Next()
class Ask():
    def __init__(self):
        pass
    def InitiateKeyMapping(self):
        GM.keyMapping.BuildKeyMapping("rest", KeyMethods.OnRest)
        GM.keyMapping.BuildKeyMapping("showans", KeyMethods.OnShowans)
    def Next(self):
        GM.progress += 1
        GM.wrongCntDown = 2
        GM.timer.ResetQ()
        if GM.wrongCntDown > 0:
            GM.scoreCal.AddCorrect()
    def Pass(self, ans):
        GM.qs[GM.progress].anses.remove(ans)
        GM.wrongCntDown = 2
        GM.timer.ResetQ()
        if len(GM.qs[GM.progress].anses) == 0:
            GM.progress += 1
            if GM.wrongCntDown > 0:
                GM.scoreCal.AddCorrect()
    def Run(self):
        while GM.progress < len(GM.qs):
            currentQuestion = GM.qs[GM.progress]
            tuple = GM.keyMapping.Input(currentQuestion.GetQuestion())
            ans = tuple[0]
            state = tuple[1]
            if state == "None":
                if currentQuestion.Check(ans) == False:
                    GM.wrongCntDown -= 1
                    if GM.wrongCntDown > 0:
                        print("Wrong, %d chances left" % GM.wrongCntDown)
                    else:
                        print("You won't get this score")
                        if GM.wrongCntDown == 0:
                            mistake = mistakeRec.Mistake(GM.selectedFile, currentQuestion.GetContent())
                            mistakeRec.Add(mistake)
                else:
                    if currentQuestion.passingMode == PassingMode.any:
                        self.Next()
                    elif currentQuestion.passingMode == PassingMode.all:
                        self.Pass(ans)