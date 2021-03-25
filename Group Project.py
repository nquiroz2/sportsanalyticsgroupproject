#!/usr/bin/env python
# coding: utf-8

# # Sports Anaytics Group Project
# By: Daniel Leal, Hannah Santa Maria, Nathalie Quiroz and Jiatai Xie
# 

# In[1]:


# download packages needed
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
plt.style.use('fivethirtyeight')


# In[ ]:





# In[2]:


# read csv file
nba_20162020 = pd.read_csv("https://raw.githubusercontent.com/nquiroz2/sportsanalyticsgroupproject/main/NBA_2016-21_pergame.csv")
nba_20162020


# In[3]:


# pandas melt function
melt_df = pd.melt(nba_20162020, id_vars='TEAM')
# view melt_df
#melt_df
# check melt_df counts
melt_df['TEAM'].value_counts()


# In[4]:


nba_20162020.describe().round(3)


# In[5]:


#calculate average 3PA for each season 
Avg3PA_PerSeason = nba_20162020.groupby('Season')['3PA'].mean().round(3)
Avg3PA_PerSeason


# In[6]:


# Plot NBA Average 3PA per Game by Season
ax = (Avg3PA_PerSeason.plot(title='NBA Average 3PA per Game by Season'))
ax.set_ylabel('Average 3PA per Game')
ax.set_xlabel('Season')
#plt.xticks(rotation = 45)


# In[13]:


# games won vs 3PA Graph


# In[8]:


nba_20162020


# In[9]:


# query() method to filter 2020-2021 Season
season_2021 = nba_20162020.query("Season==2020-2021")
season_2021


# In[11]:


# replace dashes with underscore
nba_20162020['Season'] = nba_20162020['Season'].str.replace('-','_')
nba_20162020


# In[12]:


# query() method to filter 2020-2021 Season
season_2021 = nba_20162020.query("Season==2020_2021")
season_2021


# In[ ]:




