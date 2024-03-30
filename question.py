class PassingMode:
    any = 0
    all = 1
class Question:
    def __init__(self, content = "", anses = [], wordClass = "", passingMode = PassingMode.any):
        self.content = content
        self.anses = anses
        self.wordClass = wordClass
        self.passingMode = passingMode
    def Check(self, ans):
        if ans in self.anses:
            return True
        return False
    def AddAns(self, ans):
        self.anses.append(ans)

    def GetContent(self):
        return self.content
    def GetQuestion(self):
        return self.content + " " + self.wordClass + '.' + ':'