#!/usr/bin/env python
# coding: utf-8

# CATEGORICAL DATA PLOTS

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# In[2]:


df=sns.load_dataset("tips")  # Load the tips dataset

# 

# In[5]:


sns.countplot(df['sex'])


# In[6]:


sns.countplot(x = df['sex'])

# In[7]:


sns.countplot(x = df['sex'], hue = df['smoker'])

# In[11]:


sns.barplot(x = df['sex'], y=df['total_bill'])

# In[12]:


sns.boxplot(x ='tip' , y = 'day', data = df)

# In[13]:


sns.violinplot(x ='tip' , y = 'day', data = df)

# In[14]:


sns.stripplot(x ='tip' , y = 'day', data = df)

# In[15]:


sns.swarmplot(x ='tip' , y = 'day', data = df)

# In[17]:


sns.violinplot(x ='tip' , y = 'day', data = df)
sns.swarmplot(x ='tip' , y = 'day', data = df)

# In[ ]:



