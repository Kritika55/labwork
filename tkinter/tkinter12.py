from tkinter import *
root = Tk()
#to rename the title of the window 
root.title("GUI")
mybutton = Button(root, text = "Click me",fg="red",bg = "yellow")
#pack is used to show the object in the window
mybutton.pack()
root.mainloop()