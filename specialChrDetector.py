class SpecialChrDetector:
    def __init__(self, string):
        self.string = string
    def GetType(self):
        result = "None"
        if self.string[0] == '-':
            result = "WordClass"
        elif self.string[0] == '*':
            result = "Repeating"
        return result