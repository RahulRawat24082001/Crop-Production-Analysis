#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[9]:


data = pd.read_csv('C:/Users/rawat/Downloads/Crop Production data.csv')


# In[3]:


data


# In[5]:


data.isna().sum()


# In[6]:


data['Production']


# In[7]:


data.dtypes


# In[10]:


df_ffill = data.fillna(method='ffill')


# In[13]:


df_ffill


# In[20]:


data = df_ffill


# In[21]:


data.isna().sum()


# In[23]:


data.to_csv("C:/Users/rawat/Desktop/Crop Production Analysis in India/Crop Production.csv", index = False)


# In[ ]:




