strText = "d lalal lal lala lalala la la"
def listSplitMe(strText):
    listText = strText.split()
    strWrite = ""
    lastLine = ""
    
    for i in range(0,len(listText)):
        if len(lastLine)+ len(listText[i])>9:
            strWrite+=lastLine+"\n"
            lastLine = listText[i]
            if i == len(listText)-1:
                strWrite+=lastLine
        else:
            if i == 0:
                lastLine+=listText[i]
            else:
                lastLine+=" " + listText[i]
            if i == len(listText)-1:
                strWrite+=lastLine
            
    return strWrite.split(sep="\n")

print(listSplitMe(strText))