#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from plotly.offline import iplot, init_notebook_mode



# In[28]:


init_notebook_mode(connected=True)
tips = sns.load_dataset('tips')
tips

# In[31]:


fig = px.scatter(tips, x='total_bill', y='tip', color='smoker', size='size',
                 hover_data=['day'])
fig.show()

# In[ ]:




# In[ ]:



