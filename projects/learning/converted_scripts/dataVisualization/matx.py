#!/usr/bin/env python
# coding: utf-8

# MATRIX PLOTS
# 

# In[ ]:


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


flights = sns.load_dataset('flights')
flights

# In[5]:


tips=sns.load_dataset('tips')
tips

# CLUSTER MAP

# In[7]:


tipscorr = tips[['total_bill','tip','size']]
tipscorr

# In[ ]:


tipscorr.corr()  # compute correlation matrix

# In[15]:


sns.heatmap(tipscorr.corr(), annot = True)

# In[17]:


sns.clustermap(tipscorr.corr(), annot = True)

# PIVOT TABLE

# In[18]:


pvtflights = flights.pivot(index='month', columns='year', values='passengers')
pvtflights

# In[21]:


sns.heatmap(pvtflights)

# In[22]:


sns.heatmap(pvtflights, cmap='Blues')

# In[ ]:



