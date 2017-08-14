#!c:\Python34\python

import csv

newRow = ''
timeRow = ''
myIntList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
f = open('file1.csv')
fileCont = csv.reader(f)

for i in fileCont:
    if len(i) > 0:
        itemVar = i[0]
        if itemVar[:1] == '.' or itemVar == '\n':
            '''newRow = ''
            timeRow = '''''
            print('in . -> ',itemVar)
        elif itemVar[:1] not in myIntList:
            newRow = newRow+';'+itemVar
            print('In Not -> ', itemVar)
        elif itemVar[:1] in myIntList:
            timeRow = timeRow+';'+itemVar
            print('In Int -> ', itemVar)

        '''print('In Last Else -> ', itemVar)
        newRow = newRow+';'+timeRow
        print('-----------------------------------------------------------------------------------')
        print(newRow)
        print('-----------------------------------------------------------------------------------')
        '''

f.close()