#!c:\Python34\python

from tkinter import filedialog
from tkinter import messagebox
import csv


def chooseFile(fileFlag):
    fileName = ''
    whileFlag = False
    while whileFlag == False:
        if fileFlag == 'source':
            fileName = filedialog.askopenfilename(initialdir='%SystemDrive%/Users/%username%', title='Select csv Source File')
        elif fileFlag == 'target':
            fileName = filedialog.asksaveasfilename(initialdir='%SystemDrive%/Users/%username%', title='Save csv Target File')
        if len(fileName) > 0:
            whileFlag = True
        else:
            resVar = messagebox.askquestion('Cancelation Alert', 'Do You Want To Exit The App . . .')
            if resVar == 'yes':
                exit(0)
            elif resVar == 'no':
                whileFlag = False
    return fileName

def createTargetCsv(sourceFile, targetFile):
    nameVar = ''
    timeVar = ''
    n = 0
    inFile = open(sourceFile)
    outFile = open(targetFile, 'w')
    fileCont = csv.reader(inFile)

    for fileRow in fileCont:
        tVar = ''.join(fileRow)
        if n > 3 and tVar[:1].isalpha() == True:
            outFile.write(nameVar + timeVar + '\n')
            nameVar = ''
            timeVar = ''
            n = 0
        if tVar[:1].isalpha() == True:
            n = n + 1
            nameVar += tVar + ';'
        if tVar[:1].isdigit() == True:
            timeVar += tVar + ';'
            n = n + 1
    outFile.write(nameVar + timeVar + '\n')
    inFile.close()
    outFile.close()


sourceFile = chooseFile('source')
outFile = chooseFile('target')
createTargetCsv(sourceFile, outFile)
messagebox.showwarning('File Created', 'Process Ended')

