#!/usr/bin/env python
# coding: utf-8

# OpenPyXL is a Python library used to read, write, and manipulate Excel files in the  format (Excel 2010 and later). It’s one of the most popular tools for handling spreadsheets programmatically when you don’t want to manually open Excel.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# In[3]:


df = pd.read_csv("D:\GIT WORK AND STUDY\instagram_usage_lifestyle.csv")
df.head()

# In[6]:


df.columns

# In[25]:


df.info()

# In[26]:


df.describe() 
# daily_activity_minutes wil be main to analyze
#OTHER IMPORTANT COLUMNS:
# reels_watched_per_day
# time_on_feed_per_day , time_on_explore_per_day , time_on_messages_per_day , time_on_reels_per_day
# average_session_length_minutes


# In[27]:


df.isna().sum()
# no missing values

# In[7]:


miss=df.isna().sum().sort_values(ascending=False)

# In[ ]:


sns.set_style("whitegrid")  
sns.set_palette("dark")  
sns.histplot(df['daily_active_minutes_instagram'], bins=20, kde=True)
plt.title("Distribution of Daily Active Minutes on Instagram", fontsize=14)
plt.xlabel("Daily Active Minutes", fontsize=12)
plt.ylabel("User Count", fontsize=12)

# In[ ]:


df["activity_bin"] = pd.cut(
    df["daily_active_minutes_instagram"],
    bins=[0, 100, 200, 300, 400, 500],
    labels=["0–100", "100–200", "200–300", "300–400", "400–500"]
)
sns.countplot(data=df, x="gender", hue="activity_bin")
plt.title("Instagram Activity by Gender")
plt.xlabel("Gender")
plt.ylabel("User Count")
plt.legend(title="Daily Active Minutes")
plt.show()



# In[9]:


df.corr(numeric_only=True)
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12, 8))

# In[ ]:


plt.figure(figsize=(8,6))
ax = sns.barplot(
    x='activity_bin', 
    y='reels_watched_per_day', 
    data=df, 
    ci=None, 
    palette="Spectral",   # Vibrant color palette
    edgecolor="black"     # Crisp bar edges
)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                xytext=(0, 5), 
                textcoords='offset points',
                fontsize=10, fontweight='bold', color='black')

plt.title("🔥 Average Reels Watched per Day by Activity Bin 🔥", fontsize=14, fontweight='bold', color="#333")
plt.xlabel("⏱️ Daily Active Minutes Bin", fontsize=12, color="#555")
plt.ylabel("📱 Average Reels Watched per Day", fontsize=12, color="#555")
plt.xticks(rotation=30, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# In[ ]:


plt.figure(figsize=(9,6))
ax = sns.barplot(
    x='employment_status',
    y='daily_active_minutes_instagram',
    data=df,
    ci=None,
    palette="Spectral",   
    edgecolor="black"     
)
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', 
                xytext=(0, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color='black')

plt.title("📱 Daily Instagram Activity by Employment Status", fontsize=15, fontweight='bold', color="#333")
plt.xlabel("Employment Status", fontsize=12, color="#555")
plt.ylabel("Average Daily Active Minutes", fontsize=12, color="#555")

plt.xticks(rotation=30, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()




# In[ ]:


plt.figure(figsize=(10, 6))  

ax = sns.barplot(
    x='age',
    y='daily_active_minutes_instagram',
    data=df_filtered,         
    palette='Set2',
    edgecolor='black'
)

# value labels on top of each bar
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.1f}', 
                (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color='black')

# Titles and labels
plt.title("📱 Instagram Activity by Age (5-Year Gaps)", fontsize=15, fontweight='bold')
plt.xlabel("Age", fontsize=12)
plt.ylabel("Daily Active (Minutes)", fontsize=12)

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


# In[ ]:


plt.figure(figsize=(10, 6))  

ax = sns.barplot(
    x='education_level',
    y='daily_active_minutes_instagram',
    data=df,
    palette='dark',
    edgecolor='black'
)

# value labels on top of each bar
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.1f}', 
                (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color='black')

# Titles and labels
plt.title("📚 Instagram Activity by Education Level", fontsize=15, fontweight='bold')
plt.xlabel("Education Level", fontsize=12)
plt.ylabel("Avg Daily Active Minutes", fontsize=12)

# 🧾 Rotate x-axis labels if needed
plt.xticks(rotation=30, fontsize=11)
plt.yticks(fontsize=11)

# 🧩 Add grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()


# In[ ]:


plt.figure(figsize=(10,6))

ax = sns.violinplot(
    x="education_level", 
    y="likes_given_per_day", 
    data=df, 
    palette="muted", 
    inner="quartile"
)

group_stats = df.groupby("education_level")["likes_given_per_day"].agg(['mean','max']).reset_index()

for i, row in group_stats.iterrows():
    # Average
    ax.annotate(f'Avg: {row["mean"]:.1f}', 
                xy=(i, row["mean"]), 
                xytext=(0,5), textcoords='offset points',
                ha='center', color='blue', fontsize=9, fontweight='bold')
    
    # Max
    ax.annotate(f'Max: {row["max"]}', 
                xy=(i, row["max"]), 
                xytext=(0,-15), textcoords='offset points',
                ha='center', color='red', fontsize=9, fontweight='bold')

# Titles and labels
plt.title("🎻 Likes Given per Day by Education Level (with Avg & Max)", fontsize=15, fontweight="bold")
plt.xlabel("Education Level", fontsize=12)
plt.ylabel("Likes Given per Day", fontsize=12)

plt.xticks(rotation=30, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()



# In[ ]:




plt.figure(figsize=(8,6))

ax = sns.boxplot(
    x="gender",
    y="ads_clicked_per_day",
    data=df,
    palette="dark",     
    linewidth=2.5,           
    fliersize=4             
)

group_stats = df.groupby("gender")["ads_clicked_per_day"].agg(['mean','max']).reset_index()

for i, row in group_stats.iterrows():
    # Average
    ax.annotate(f'Avg: {row["mean"]:.1f}', 
                xy=(i, row["mean"]), 
                xytext=(0,5), textcoords='offset points',
                ha='center', color='white', fontsize=10, fontweight='bold')

# Titles and labels
plt.title("Spending Behavior by Gender (Ads Clicked per Day)", fontsize=16, fontweight="bold", color="#333")
plt.xlabel("Gender", fontsize=13)
plt.ylabel("Ads Clicked per Day", fontsize=13)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()

# In[ ]:


plt.figure(figsize=(10,6))

ax = sns.barplot(
    x="relationship_status",
    y="dms_sent_per_week",
    data=df,
    palette="dark",      
    edgecolor="black",
    ci=None                   
)

# Add value labels on top of bars
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height:.1f}', 
                (p.get_x() + p.get_width() / 2., height), 
                ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points',
                fontsize=10, fontweight='bold', color='black')

# Titles and labels
plt.title("💬 DMs Sent per Week by Relationship Status", fontsize=15, fontweight="bold")
plt.xlabel("Relationship Status", fontsize=12)
plt.ylabel("DMs Sent per Week", fontsize=12)

plt.xticks(rotation=30, fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# In[ ]:


plt.figure(figsize=(9,6))

# Base scatter plot
sns.scatterplot(
    x="weekly_work_hours",
    y="user_engagement_score",
    data=df,
    hue="employment_status",    
    size="age",                 
    palette="dark",
    alpha=0.7,
    edgecolor="black"
)

# Add regression line to show trend
sns.regplot(
    x="weekly_work_hours",
    y="user_engagement_score",
    data=df,
    scatter=False,
    color="gray",
    line_kws={"linestyle":"--", "linewidth":2}
)

plt.title(" Weekly Work Hours vs Engagement Score", fontsize=15, fontweight="bold")
plt.xlabel("Weekly Work Hours", fontsize=12)
plt.ylabel("User Engagement Score", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# In[7]:


plt.figure(figsize=(9,6))

# Hexbin plot
plt.hexbin(
    df["weekly_work_hours"], 
    df["user_engagement_score"], 
    gridsize=30,          # controls hex size (smaller = more detail)
    cmap="Spectral",      # bold color palette
    mincnt=1              # only show bins with at least 1 point
)

# Add colorbar to show density
plt.colorbar(label="Count in bin")

# Titles and labels
plt.title("Hexbin Plot: Weekly Work Hours vs Engagement Score", fontsize=15, fontweight="bold")
plt.xlabel("Weekly Work Hours", fontsize=12)
plt.ylabel("User Engagement Score", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# In[ ]:



