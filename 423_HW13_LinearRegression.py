#!/usr/bin/env python
# coding: utf-8

# ## Q1. (6 Points)

# An analyst in Phidelity Investments wants to develop a regression model to predict the annual rate of return for a stock based on the price-earnings (PE) ratio of the stock and a measure of the stock's risk. The data found in the file Phidelity.xlsx were collected for a random sample of stocks. 

# Q1.1. First read the data from the file. 

# In[1]:


#!pip3 install statsmodels
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

with pd.ExcelFile('Phidelity.xlsx') as xls:
    df = pd.read_excel(xls, 'Data')


# In[2]:


# show the top 10 rows of the data
df.head(10)


# Q1.2. Plot scatter plot for each independent variable versus dependend variable.

# In[3]:


Y = df['Return']
X = df['PE Ratio'] 
plt.scatter(X,Y)  # scatter of PE vs. Return


# In[4]:


Y = df['Return']
X = df['Risk'] 
plt.scatter(X,Y)  # scatter of Risk vs. Return


# Q1.3. Conduct a regression model for the following equation.
# $Y = b_0 + a X_1 + b X_2$ where $Y$ is Return, $X_1$ is PE Ratio, and $X_2$ is Risk.

# In[5]:


Y = df['Return']
X = df[['PE Ratio', 'Risk']]
Model = smf.ols('Y~X', data = df).fit()
print(Model.summary) # print summary of the model


# In[6]:


print(Model.params) # print parameters of the model


# Q1.4: Conduct a regression model for the following equation.
# $Y = b_0 + a X_1 + b X_2 + c X_3 + d X_4 $
# where $Y$ is Return, $X_1$ is PE Ratio, and $X_2$ is Risk, $X_3$ is $X_1^2$ and $X_4$ is $X_2^2$.

# In[7]:


Y = df['Return']
# add a new column called 'X3' whoch is PE Ratio^2
df['X3'] = pd.Series(df['PE Ratio']**2)
# add a new column called 'X4' whoch is Risk^2
df['X4'] = pd.Series(df['Risk']**2)


# In[8]:


df.head(10)


# In[10]:


# build the model here:
X = df[['PE Ratio', 'Risk', 'X3', 'X4']]
Model2 = smf.ols('Y~X', data=df).fit()
print(Model2.summary()) # print summary of the model


# In[11]:


print(Model2.params) # print parameters of the model


# ## Q2. (4 points)

# The following code downloads the stock price of `Apple` from `Yahoo Finance` (from Jan. 1, 2010). You can download the stockprice of other corporations as well by adding them as string in to the variable `CoList`. `StPrice` is the variable that holds the price of stock. Apply `moving average` using 3 and 5 time periods.  

# In[1]:


get_ipython().system('pip3 install yahoo_fin')


# In[4]:


CoList =["AAPL"]
#"APC","8356B",
import numpy as np
import pandas as pd
from yahoo_fin import stock_info as si
StData={}
StPrice=[]
i =0
while i < len(CoList):
    StockData0 = si.get_data(CoList[i],start_date = '01/01/2010')
    StData[str(CoList[i])]=np.array(StockData0['adjclose'])
    index = StockData0.index
    if i ==0:
        StPrice=pd.DataFrame({str(CoList[i]):StData[str(CoList[i])]},index)
    else:
        df1=pd.DataFrame({str(CoList[i]):StData[str(CoList[i])]},index)
        StPrice=pd.concat([StPrice,df1],  axis=1)
        
    i= i+ 1
print(StPrice.head())


# In[5]:


import matplotlib.pyplot as plt
plt.plot(StPrice)
plt.show()


# In[8]:


# 3- day moving average: Write your code below:
StPrice.rolling(3).mean().plot()


# In[10]:


# plot 3-day moving average vs the original data
StPrice.rolling(3).mean().plot(c = 'red')
StPrice.plot( c = 'blue')


# In[9]:


# 5- day moving average: Write your code below:
StPrice.rolling(5).mean().plot()


# In[13]:


# plot 5-day moving average, 3-day moving average, and the original data
StPrice.rolling(5).mean().plot(c = 'green')
StPrice.rolling(3).mean().plot(c = 'red')
StPrice.plot( c = 'blue')


# In[ ]:




