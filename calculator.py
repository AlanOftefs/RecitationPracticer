class Calculator():
    def __init__(self):
        self.correctNum = 0
    def AddCorrect(self):
        self.correctNum += 1
    def Refresh(self):
        self.correctNum = 0