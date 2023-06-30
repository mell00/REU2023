# import everything from tkinter module
from tkinter import *
  
# import messagebox from tkinter module
import tkinter.messagebox
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("When you press a any button the message will pop up")
root.geometry('500x300')
  
# Create a messagebox showinfo
  
def East():
    tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")
  
def West():
    tkinter.messagebox.showinfo("Welcome to GFG", "West Button clicked")
  
def North():
    tkinter.messagebox.showinfo("Welcome to GFG", "North Button clicked")
  
def South():
    tkinter.messagebox.showinfo("Welcome to GFG", "South Button clicked")
  
# Create a Buttons
  
Button1 = Button(root, text="West", command=West, pady=10)
Button2 = Button(root, text="East", command=East, pady=10)
Button3 = Button(root, text="North", command=North, pady=10)
Button4 = Button(root, text="South", command=South, pady=10)
  
# Set the position of buttons
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)
Button3.pack(side=TOP)
Button4.pack(side=BOTTOM)
  
root.mainloop()