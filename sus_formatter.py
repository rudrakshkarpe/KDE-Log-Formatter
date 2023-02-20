#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('log_sus.csv', sep=';', header=None, names=["Iterations", "Start-time","Empty", "Description"])
df.drop(columns=['Empty'], inplace=True)
df.head()


# In[4]:


df['Start-time'] = pd.to_datetime(df['Start-time'])
df['End-time'] = df['Start-time'].shift(-1)


# In[5]:


df.head()


# In[24]:


df['Duration(sec)'] = (df['End-time'] - df['Start-time']).dt.total_seconds()
df['Elapsed(sec)'] = (df['Start-time'] - df['Start-time'].min()).dt.total_seconds()
df.head()


# In[25]:


df.to_csv('log_sus_duration.csv', sep=';', header=None, index=False)


# In[26]:


df.head(46)


# In[ ]:




