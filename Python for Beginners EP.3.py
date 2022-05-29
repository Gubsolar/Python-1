from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x300+500+250')


B1 = Button(GUI,text = 'hello')
B1.pack(ipadx = 50,ipady = 20)

F1 = Frame(GUI)
F1.place(x = 20,y = 50)

B1 = ttk.Button(F1,text = 'hello2')
B1.pack(ipadx = 50,ipady = 20)


GUI.mainloop()