import csv, os
from tkinter import *

def openCommand():
    pass

def saveCommand():
    pass

def closeCommand():
    pass



result = {}
textBlob = ""
csvDict = os.popen('systeminfo /FO CSV')
dictReader = csv.DictReader(csvDict)
csvHeaderList = os.popen('systeminfo /FO CSV')
reader = csv.reader(csvHeaderList)
headers = next(reader, None) #3.x specific call to 'next' iterator





for row in dictReader:
    for column, value in row.items():
        result.setdefault(column, []).append(value)
        #print('KEY:', column, '  VALUE:', str(value))

for header in headers:
    #print(header, ': ', str(result.get(header)).strip("'[]'"))
    textBlob += header + ": " + str(result.get(header)).strip("'[]'") + "\n"


#create window, remove ico, and set title
mainWindow = Tk()
mainWindow.title('Windows System Info')

#create the pull down menu bar on the mainWindow
menuBar = Menu(mainWindow)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='Open', command=openCommand)
fileMenu.add_command(label='Save', command=saveCommand)
fileMenu.add_command(label='Close', command=closeCommand)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=mainWindow.quit)
menuBar.add_cascade(label='File', menu=fileMenu)

#display the menu

mainWindow.config(menu=menuBar)
lbl = Label(mainWindow, text = textBlob)
lbl.pack()
mainWindow.mainloop()
