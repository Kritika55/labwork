from tkinter import *
root = Tk()
#to rename the title of the window
root.title("GUI")
myLabel = Label(root, text = "Tkinter",font=("Arial Bold", 50))
#pack is used to show the object in the window
myLabel.pack()
root.mainloop()