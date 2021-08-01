#!/usr/bin/env python
# coding: utf-8

# ## QUESTION 1 

# In[ ]:


#Write a program that: 
#asks the user for a number
#the program should display all positive factors of the number that is input.


# In[10]:


x = int(input("Enter your num: "))
counter = 0
comma = ""
top = []
sum = 0
for i in range (1, (x+1)):
    if(x % i == 0):
        counter = counter + 1
        print(comma, i, end='')
        comma = ','
        if(counter < 4):
            top.append(i)
            sum += i
print('\n Number of factors: ', counter)
print('Top 3: ', top)
avg = float(sum)/3
print('Average is: ', avg)


# In[ ]:





# ## QUESTION 2

# In[ ]:


#write a program that accepts a list with different length
#identify and eliminate the duplicated values
#display a message


# In[17]:


mylist = ['joe','jack','joe','joe','sarah']
print("Given list")
print(mylist)
ans = []

for value in mylist:
   if value not in ans:
       ans.append(value)
print("\nValue and their count")
for value in ans:
   if mylist.count(value) > 1:
       print(value," ",mylist.count(value))
print("\nAfter elimination of duplicates")
print(ans)


# ## QUESTION 3

# In[ ]:


#write a program that asks a users bday in MM/DD/YYYY format 
#and return the month of the users' birthdate


# In[33]:


def find_month(dob):
    month, date, year = dob.split('/')
    if month == '01':
        return 'January'
    elif month == '02':
        return 'February'
    elif month == '03':
        return 'March'
    elif month == '04':
        return 'April'
    elif month == '05':
        return 'May'
    elif month == '06':
        return 'June'
    elif month == '07':
        return 'July'
    elif month == '08':
        return 'August'
    elif month == '09':
        return 'September'
    elif month == '10':
        return 'October'
    elif month == '11':
        return 'November'
    elif month == '12':
        return 'December'

dob = input('Enter your date of birth (MM/DD/YYYY): ')
print('Month of your birthdate is:', find_month(dob))


# ## QUESTION 4

# In[ ]:


#write a program that reads
#for each agent find the average over the past 12 months
#plot the sales of each agent
#graphs should have enough information


# In[34]:


import csv
filename = input('Enter file name ')

try:
    with open(filename) as f:
        content = csv.reader(f)
        header_row = next(content) 
        
        DictA={}
        for row in content:   
            y=row[0].split('\t') 
            DictA[y[0]]=[float(x) for x in y[1:12]] 
            
        
        
        import matplotlib.pyplot as plt 
        get_ipython().run_line_magic('matplotlib', 'inline')

        for agents in DictA.keys():
            plt.figure(figsize =(20,2))
            plt.plot(DictA[agents]) 
            plt.xlabel('Month', fontsize = 10)
            plt.ylabel('Total Sales', fontsize = 10)
            plt.legend(DictA.keys()) 
except FileNotFoundError:
    print('File not found')


# ## QUESTION 5

# In[ ]:


#prepare 5 scatter plots
#Which independent variables would you consider in the regression model
#create a regression model based on x2 and x5


# ## SECTION A

# In[39]:


import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

with pd.ExcelFile('Construction.xlsx') as xls:
    df = pd.read_excel(xls, 'Bid History')


# In[40]:


df.head(10)


# In[41]:


Y = df['Total Cost']
X = df['Units of Work']
plt.scatter(X,Y)


# In[42]:


Y = df['Total Cost']
X = df['Contracted Units per Day']
plt.scatter(X,Y)


# In[43]:


Y = df['Total Cost']
X = df['Level of Equipment Required']
plt.scatter(X,Y)


# In[44]:


Y = df['Total Cost']
X = df['Wage - Regular (0) or Premium (1)']
plt.scatter(X,Y)


# In[45]:


Y = df['Total Cost']
X = df['City']
plt.scatter(X,Y)


# ## SECTION B
# 
# Which independent variables would you consider in your regression model? Create a
# regression model
# 
# ANSWER:I would choose model 
# Y = df['Total Cost']
# X = df['Units of Work']
# because it has the highest Adj. R-square at 0.804

# In[46]:


#I WOULD CONSIDER THIS MODEL BECAUSE IT HAS THE HIGHEST ADJ. R SQUARED AT 0.804

Y = df['Total Cost']
X = df['Units of Work']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[47]:


Y = df['Total Cost']
X = df['Contracted Units per Day']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[48]:


Y = df['Total Cost']
X = df['Level of Equipment Required']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[49]:


Y = df['Total Cost']
X = df['Wage - Regular (0) or Premium (1)']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[50]:


Y = df['Total Cost']
X = df['City']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# ## SECTION C
# Create a regression model based on X2 and X5. Then compare this regression model with
# the one you created in the section b.
# 
# ANSWER: The regression model based on X2 and X5 was my selected model for section b because it had the highest adj. R-square so it is the same model and all the R statistics are the same. There are differences if we put Units of Work as the Y and Total Cost as the X as the std error decreases for model 2 and it has a negative coefficient.

# In[51]:


Y = df['Total Cost']
X = df['Units of Work']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[52]:


Y = df['Units of Work']
X = df['Total Cost']
Model = smf.ols('Y~X', data=df).fit()
print(Model.summary())


# In[ ]:




