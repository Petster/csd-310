import tkinter as Tk
from tkinter import ttk
from tkinter import font

def createMenuFrame(container):
    menuFrame = ttk.Frame(container)
    buttonFont = font.Font(size=20)
    labelOne = Tk.Button(menuFrame, text="View Books", font=buttonFont, command= lambda: viewBooks(root, menuFrame)).grid(row=0, column=0)
    labelTwo = Tk.Button(menuFrame, text="View Store Locations", font=buttonFont).grid(row=0, column=1)
    labelThree = Tk.Button(menuFrame, text="My Account", bg='blue', fg='white', font=buttonFont).place(x=10,y=182,width=570,height=72)
    labelFour = Tk.Button(menuFrame, text="Exit", font=buttonFont, bg='red', fg='white', command=root.destroy).place(x=0,y=428,width=600,height=72)
    return menuFrame

def clearWindow(frame):
    frame.destroy()

def viewBooks(root, menuFrame):
    clearWindow(menuFrame)
    viewBookFrame = ttk.Frame(root)
    buttonFont = font.Font(size=20)
    labelFour = Tk.Button(viewBookFrame, text="Back", font=buttonFont, bg='red', fg='white', command=lambda: createMenuFrame(root)).grid(row=4, columnspan=4)
    viewBookFrame.pack()


#init tkinter
root = Tk.Tk()
root.title("WhatABook Online")
root.geometry('600x500')

start = createMenuFrame(root).grid(column=1, row=0)



root.resizable(False, False) 
root.mainloop()