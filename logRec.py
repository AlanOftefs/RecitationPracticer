#!/usr/bin/python
#-*- coding : uft-8 -*-
import datetime

_path="log"
_file="log.txt"
class ExcInfo():    
    def __init__(self, exc):        
        self.file=str(exc.__traceback__.tb_frame.f_globals["__file__"])
        self.line=str(exc.__traceback__.tb_lineno)
        self.excReason = str(exc)
    def AddTime(content : str):
        result = "%s\n%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), content)
        return result
    def LogFormat(self):        
        result = ExcInfo.AddTime("File : %s\nLine : %s\nError : %s\n" %( self.file, self.line, self.excReason))        
        return result
class Log:
    def RecordExc(exc : Exception):
        excInfo = ExcInfo(exc)
        with open("%s/%s" % (_path, _file), "a+", encoding = "utf-8") as log:
            log.write(excInfo.LogFormat())                     
            log.close()
    def RecordStr(_str : str):
        with open("%s/%s" % (_path, _file), "a+", encoding = "utf-8") as log:            
            log.write(ExcInfo.AddTime(_str) + "\n")
            log.close()
    def GetExceptionExc(exc : Exception):
        excInfo = ExcInfo(exc)
        return excInfo.LogFormat()
    def GetExceptionStr(_str : str):
        return ExcInfo.AddTime(_str)
    
    
