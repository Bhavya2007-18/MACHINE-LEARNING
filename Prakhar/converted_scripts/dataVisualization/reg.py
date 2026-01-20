#!/usr/bin/env python
# coding: utf-8

# REGRESSION PLOTS

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[2]:


tips = sns.load_dataset('tips')
tips

# In[4]:


sns.lmplot(x= 'total_bill', y= 'tip', data= tips)

# In[5]:


sns.lmplot(x= 'total_bill', y= 'tip', data= tips, hue='sex')

# In[ ]:



