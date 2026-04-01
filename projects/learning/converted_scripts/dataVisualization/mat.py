#!/usr/bin/env python
# coding: utf-8

# BASICS

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[6]:


x= np.linspace(0,5,11)
x
y= x **3
y

# In[8]:


plt.plot(x,y)
plt.title("PLOT OF X VS Y")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

# SUBPLOTS
# 

# In[10]:


plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.plot(x,x**2)
plt.subplot(2,2,4)
plt.plot(y,y**2)

# OBJECT OREINTATED WAY

# In[23]:


fig= plt.figure()
axis1=fig.add_axes([0.1,0.1,0.8,0.8])  # left,bottom,width,height
axis1.plot(x,y)
axis2=fig.add_axes([0.3,0.5,0.2,0.2])  # left,bottom,width,height
axis2.plot(y,x)
plt.savefig("1st_plot.png")


# TYPES OF PLOTS

# In[18]:


plt.scatter(x,y)  # scatter plot

# In[19]:


plt.hist(x)  # histogram

# In[20]:


plt.boxplot(y)  # box plot

# WORKING WITH IMAGES

# In[24]:


import matplotlib.image as mpimg
img= mpimg.imread("1st_plot.png")
plt.imshow(img)



# In[ ]:



