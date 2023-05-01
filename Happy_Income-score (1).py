#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().system('pip install potly')


# In[3]:


df=pd.read_csv('happyscore_income.csv')


# In[4]:


df.head()


# In[5]:


# Create a scatter plot of Average Income vs. HappyScore
plt.scatter(df['avg_income'], df['happyScore'])
plt.xlabel('Average Income')
plt.ylabel('HappyScore')
plt.title('Average Income vs. HappyScore')
plt.show()


# In[6]:


# Create a box plot of Income by Region
df.boxplot(column='avg_income', by='region')
plt.xticks(rotation=90)
plt.title('Income by Region')
plt.show()


# In[7]:


# Create a bar plot of the top 10 countries with highest HappyScore
top_happy = df.sort_values('happyScore', ascending=False).head(10)
plt.bar(top_happy['country'], top_happy['happyScore'])
plt.xticks(rotation=90)
plt.xlabel('Country')
plt.ylabel('HappyScore')
plt.title('Top 10 countries with highest HappyScore')
plt.show()


# In[8]:


# Create a histogram of GDP 
plt.hist(df['GDP'])
plt.xlabel('GDP')
plt.ylabel('Frequency')
plt.title('Histogram of GDP')
plt.show()


# In[9]:


# Create a scatter plot of Income vs. HappyScore with region coloring
sns.scatterplot(data=df, x='avg_income', y='happyScore', hue='region')
plt.xlabel('Average Income')
plt.ylabel('HappyScore')
plt.title('Average Income vs. HappyScore by Region')
plt.show()


# In[12]:


import matplotlib.pyplot as plt

# Extract data
x = df.groupby('region')['avg_income'].mean().sort_values(ascending=False)

# Create bar plot
plt.bar(x.index, x)

# Add title and axis labels
plt.title('Average Income by Region')
plt.xlabel('Region')
plt.ylabel('Average Income')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Display plot
plt.show()

