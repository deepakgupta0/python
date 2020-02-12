#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
def clicked():
    try:
        ans=int(txt.get())
    except:
        lbl.configure(text="PLEASE ENTER VALID INTEGER INPUT")
    lbl.configure(text = ans**2)
window = Tk()
window.title("Welcome to app")
window.geometry('350x200')
lbl=Label(window,text="ANSWER")
lbl.grid(column=3,row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="ADD", bg="red", fg="black",command=clicked)
btn.grid(column=2, row=0)

window.mainloop()


# In[33]:


from tkinter import *
from tkinter import messagebox
ls=[]
def clicked():
        try:
            ans=int(txt.get())
            ls.append(ans)
        except:
            messagebox.showinfo('ERROR!!!!!!!', "ENTER NUMBERS ONLY!!!")
        txt.delete(first=0,last=4)           
        text = lbl.cget("text") + str(ans)
        lbl.configure(text=text + " ")
def Sum_clicked():
    if sum(ls)==0:
        messagebox.showinfo("info","NO NUMBERS PRESENT IN YOUR LIST")
    else:
        messagebox.showinfo('SUM_OF_THE_GIVEN_NOS', sum(ls))
    
def Reset_clicked():
    ls.clear()
    lbl.configure(text="")
    
    

window = Tk()
window.title("Welcome to app")
window.geometry('350x200')
lbl = Label(window,text="")
lbl.pack()
lbl.grid(column=0,row=3)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn1 = Button(window, text="ADD", bg="white", fg="black",command=clicked)
btn1.grid(column=2, row=0)
btn2 = Button(window, text="RESET", bg="white", fg="black",command=Reset_clicked)
btn2.grid(column=3, row=0)
btn3 = Button(window, text="SUM", bg="white", fg="black",command=Sum_clicked)
btn3.grid(column=4, row=0)

window.mainloop()


# In[ ]:




