#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
from pymongo import MongoClient


# In[2]:


client = MongoClient('mongodb+srv://admin:raichu554@cluster0.iwukc.mongodb.net/weather_climate?retryWrites=true&w=majority')
db_name = client.weather_climate
collection = db_name.hourly_weather
print(client)


# In[3]:


x = collection.find()

docs = list(x)
print(docs)


# In[4]:


import pprint
pprint.pprint(docs)  #represent data in structured form


# In[5]:


from pandas import json_normalize  #normalizing the data in tabular form
df=json_normalize(docs)


# In[6]:


df.head()


# In[7]:


docs[1].keys()


# In[8]:


df['date'] = pd.to_datetime(df['dt'],unit="s")


# In[9]:


df.head()


# In[10]:


sns.lineplot(df['date'],df['humidity'])


# In[11]:


sns.relplot(df['date'],df['temp'])


# In[12]:


sns.distplot(df['humidity'],kde=True,bins=30)


# In[13]:


sns.distplot(df['temp'],kde=True,bins=30)


# In[14]:


sns.pairplot(data=df[['temp','humidity','pressure']])


# In[15]:


sns.lineplot(df['clouds'],df['visibility'])


# In[16]:


sns.catplot(data=df, kind="violin", x="humidity", y="wind_speed", split=True)


# In[17]:


sns.jointplot(df['temp'],df['humidity'])


# In[18]:


sns.jointplot(df['temp'],df['humidity'], kind ="hex")


# In[19]:


sns.jointplot(df['temp'],df['humidity'], kind ="kde")


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


plt.scatter(data=df, x='temp',y='humidity')
plt.xlabel('temp')
plt.ylabel('humidity')
