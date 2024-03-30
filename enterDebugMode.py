import globalManager as GM
def EnterDebugMode():
    GM.debugMode = True
    print("yes")
def Initiate():
    GM.keyMapping.BuildKeyMapping("142857", EnterDebugMode)