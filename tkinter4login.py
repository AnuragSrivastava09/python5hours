from tkinter import*
a=Tk()
l1=Label(a,text="Enter user name").grid(row=0,column=0)
e1=Entry(a)
e1.grid(row=0,column=1)
l2=Label(a,text="enter the password").grid(row=1,column=0)
e2=Entry(a)
e2.grid(row=1,column=1)
b1=Button(a,text="submit",width=20).grid(row=2,column=1)
a.mainloop()
