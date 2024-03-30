funcs = {}
class MessageCenter:
    @staticmethod
    def Add(code, func):
        funcs[code] = func
    @staticmethod
    def Invoke(code):
        try: funcs[code]()
        except: return -1