import tkinter as Tk
from tkinter import ttk
from tkinter import font

def clearWindow(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def createMenuFrame(frame):
    if(frame != "none"):
        clearWindow(frame)
        frame.grid()
    labelOne = Tk.Button(frame, text="View Books", font=buttonFont, command= lambda: viewBooks(frame)).grid(row=0, column=0)
    labelTwo = Tk.Button(frame, text="View Store Locations", font=buttonFont, command= lambda: viewLocations(frame)).grid(row=0, column=1)
    labelThree = Tk.Button(frame, text="My Account", bg='blue', fg='white', font=buttonFont, command= lambda: accountCheck(frame)).grid(row=1, column=0)
    labelFour = Tk.Button(frame, text="Exit", font=buttonFont, bg='red', fg='white', command=root.destroy).grid(row=2, column=0)
    return frame

def viewBooks(frame):
    clearWindow(frame)
    header = Tk.Label(frame, text="WhatABook's Inventory", font=buttonFont).grid(row=0, column=3, columnspan=5)
    backButton = Tk.Button(frame, text="Back", font=buttonFont, bg='red', fg='white', command= lambda: createMenuFrame(frame)).grid(row=4, columnspan=4)

def viewLocations(frame):
    clearWindow(frame)
    header = Tk.Label(frame, text="WhatABook Locations", font=buttonFont).grid(row=0, column=3, columnspan=5)
    backButton = Tk.Button(frame, text="Back", font=buttonFont, bg='red', fg='white', command= lambda: createMenuFrame(frame)).grid(row=2, columnspan=4)

def printIn(var):
    inp = var.get()
    print(inp)

def accountCheck(frame):
    clearWindow(frame)
    header = Tk.Label(frame, text="Verify Account ID", font=buttonFont).grid(row=0, column=3, columnspan=4)
    userIn = Tk.Entry(frame).grid(row=1, column=3, columnspan=4)
    userInButton = Tk.Button(frame, text="Submit", font=buttonFont, bg='green', fg='white', command= lambda: printIn(userIn)).grid(row=2, column=3, columnspan=4)
    backButton = Tk.Button(frame, text="Back", font=buttonFont, bg='red', fg='white', command= lambda: createMenuFrame(frame)).grid(row=3, column=3, columnspan=4)

def createAccountMenu(frame):
    clearWindow(frame)
    header = Tk.Label(frame, text="What would you like to do?", font=buttonFont).grid(row=0, column=3, columnspan=5)
    backButton = Tk.Button(frame, text="Back", font=buttonFont, bg='red', fg='white', command= lambda: createMenuFrame(frame)).grid(row=2, columnspan=4)

#init tkinter
root = Tk.Tk()
root.title("WhatABook Online")
root.geometry('600x500')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

buttonFont = font.Font(size=20)
mainFrame = ttk.Frame(root)
start = createMenuFrame(mainFrame).grid(row=0, column=0)



root.resizable(False, False) 
root.mainloop()