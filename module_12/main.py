import tkinter as Tk
from tkinter import ttk
from tkinter import font

#init tkinter
root = Tk.Tk()
root.title("WhatABook Online")
root.geometry('1280x720')

buttonFont = font.Font(size=25)

labelOne = Tk.Button(root, text="View Books", width=20, font=buttonFont)
labelOne.place(height=100, width=350, x=200, y=200)

labelTwo = Tk.Button(root, text="View Store Locations", width=20, font=buttonFont)
labelTwo.place(height=100, width=350, x=730, y=200)

labelThree = Tk.Button(root, text="My Account", bg='blue', fg='white', width=20, font=buttonFont)
labelThree.place(height=100, width=880, x=200, y=330)

labelFour = Tk.Button(root, text="Exit", width=10, font=buttonFont, bg='red', fg='white', command=root.destroy)
labelFour.place(height=100, width=1280, x=0, y=620)

root.resizable(False, False) 
root.mainloop()