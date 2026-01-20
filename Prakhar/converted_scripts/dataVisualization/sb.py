#!/usr/bin/env python
# coding: utf-8

# DISTRIBUTION PLOT  , used for quantitative plot

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# In[2]:


df =sns.load_dataset('tips')

# In[3]:


df['size'].unique()

# In[4]:


plt.subplot(1,2,1)
sns.histplot(df['total_bill'], bins = 20, kde = True)
plt.subplot(1,2,2)
sns.histplot(df['tip'], bins = 20, kde = True)
# its a histrogram plot

# In[5]:


sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter')
# its a scatter plot -- kind can be changed to 'hex', 'reg', 'kde' -- used in linear regression

# In[6]:


sns.jointplot(x='total_bill', y='tip', data=df, kind='reg')

# In[7]:


sns.pairplot(df)

# In[8]:


sns.pairplot(df, hue="sex")

# In[9]:


sns.rugplot(x='total_bill', y='tip', data=df) 
# least use case plot -- shows distribution of data points along an axis

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



