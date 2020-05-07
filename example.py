from tkinter import *


#This is an example of a program being made with the code
root = Tk()
root.geometry('300x300')

lbl1 = Label(root,text='Insert Web Site')
lbl1.place(x=0, y=0)
entr1 = Entry(root,text='')
entr1.place(x=0, y=30)
searchbtn = Button(root,text='Go To The Website')
searchbtn.place(x=75, y=30)







root.mainloop()
