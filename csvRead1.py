#!c:\Python34\python

import csv

nameVar = ''
timeVar = ''
n = 0
inFile = open('file1.csv')
outFile = open('out1.csv','w')
fileCont = csv.reader(inFile)

for fileRow in fileCont:
    tVar = ''.join(fileRow)
    if n > 3 and str(fileRow).isalpha() == True:
        print('PR --> ', nameVar,timeVar)
        outFile.write(nameVar+timeVar+'\n')
        nameVar = ''
        timeVar = ''
        n = 0
    if str(fileRow).isalpha() == True:
        n = n+1
        nameVar += fileRow+','
    else:
    #if tVar[:1].isdigit() == True:
        timeVar += str(fileRow)+','
        n = n+1

inFile.close()