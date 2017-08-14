#!c:\Python34\python

from winreg import *

def getListSeparator():
    '''Retrieves the Windows list separator character from the registry'''
    aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
    aKey = OpenKey(aReg, r"Control Panel\International")
    val = QueryValueEx(aKey, "sList")[0]
    return val

print(getListSeparator())