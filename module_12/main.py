import tkinter as Tk
from tkinter import ttk
from tkinter import font

#init tkinter
root = Tk.Tk()
root.title("WhatABook Online")
root.geometry('1280x720')

def createMenuFrame():
    menuFrame = ttk.Frame(root)
    buttonFont = font.Font(size=20)
    labelOne = Tk.Button(menuFrame, text="View Books", font=buttonFont).grid(row=1, column=0, columnspan=2)
    labelTwo = Tk.Button(menuFrame, text="View Store Locations", font=buttonFont).grid(row=1, column=3)
    labelThree = Tk.Button(menuFrame, text="My Account", bg='blue', fg='white', font=buttonFont).grid(row=2)
    labelFour = Tk.Button(menuFrame, text="Exit", font=buttonFont, bg='red', fg='white', command=root.destroy).grid(row=3)
    menuFrame.place(x=0, y=0)
    return menuFrame

def clearWindow(frame):
    frame.destroy()

createMenuFrame()

root.resizable(False, False) 
root.mainloop()