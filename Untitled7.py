#!/usr/bin/env python
# coding: utf-8

# In[17]:


from tkinter import*
window=Tk()
window.geometry('350x200')
window.title("Welcome to LikeGeeks app")
lbl1 = Label(window, text="Hello")
lbl2= Label(window,text="World")
lbl1.grid(row=0,column=0)
lbl2.grid(row=2,column=0)
btn = Button(window, text="Click Me", bg="red", fg="black",command=clicked)
btn.grid(column=2, row=3)
window.mainloop()


# In[16]:


def clicked():
    lbl1.grid(row=0,column=2)
    window.configure(bg="red")
    


# In[ ]:


from tkinter import *
window = Tk()
window.title("Welcome to app")
window.geometry('350x200')
lbl=Label(window,text="ANSWER")
lbl.grid(column=3,row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="Click Me", bg="red", fg="black",command=clicked)
btn.grid(column=2, row=0)
def clicked():
    ans=float(txt.get())
    lbl.configure(text = ans**2)
window.mainloop()


# In[ ]:




