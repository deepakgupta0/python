#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
t=turtle.Pen()


# In[4]:


t.forward(100)


# In[3]:


t.speed(1)


# In[5]:


t.home()


# In[6]:


t.clear()


# In[7]:


t.circle(50)


# In[8]:


t.color("red","green")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)


# In[9]:


t.end_fill()


# In[25]:


t.clear()


# In[35]:


t.home()


# In[36]:


t.clear()


# In[22]:


for i in range(0,10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    


# In[40]:


t.home()
t.clear()
t.pencolor("white")
turtle.bgcolor("black")
t.speed(0)
for i in range(1,501):
    t.forward(2*i)
    t.left(90)
    


# In[46]:


t.home()
t.clear()
turtle.bgcolor("black")
c=["red","yellow","green","blue","gold","white"]
t.speed(0)
t.width(2)
for i in range(1,501):
    t.pencolor(c[i%6])
    t.forward(2*i)
    t.left(60)
 


# In[47]:


t.home()
t.clear()
turtle.bgcolor("black")
c=["red","yellow","green","blue","gold","white"]
t.speed(0)
t.width(2)
for i in range(1,501):
    t.pencolor(c[i%6])
    t.circle(i)
    t.left(60)


# In[ ]:




