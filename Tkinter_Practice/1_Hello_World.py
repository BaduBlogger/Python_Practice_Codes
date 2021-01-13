from tkinter import *
from tkinter.ttk import *

#Creating Main window named root
root = Tk()
root.title("First Tkinter Program")	#Title of Frame, displayed on left top of the window

label = Label(root,text="Hello World").pack()

root.mainloop()	#Calling mainloop function. Tells application is ready and tells code to keep displaying 

