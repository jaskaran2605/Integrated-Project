#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv("weight_model.csv")


# In[3]:


dataset


# In[4]:


y = dataset['Weight']


# In[5]:


y


# In[6]:


x = dataset['Height']


# In[7]:


x


# In[8]:


type(x)


# In[9]:


X = x.values.reshape(3000, 1)


# In[10]:


X


# In[11]:


X.shape


# In[12]:


X.ndim


# In[13]:


from sklearn.linear_model import LinearRegression


# In[14]:


model = LinearRegression()


# In[15]:


model.fit(X, y)


# In[16]:


model.predict([[int(170)]])


# In[ ]:




