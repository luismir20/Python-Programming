#!/usr/bin/env python
# coding: utf-8

# ## Q1. pandas' basics (3 points)

# In[1]:


import pandas as pd #  import pands
import numpy as np


# Create a pandas series [1,2,3,4] with indexes 'A','B','C','D'. 

# In[4]:


# write your code here
a = pd.Series([1,2,3,4], index=['A','B','C','D'])
a


# Show elements of `a`,pandas' series, greater than 2.

# In[3]:


# write your code here
a[a>2]


# Consider the following dataframe.

# In[30]:


from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# Show columns W and X of the dataframe.

# In[6]:


# write your code here
df[['W','X']]


# Show rows A and D of the dataframe.

# In[7]:


# write your code here
df.loc[['A','D']]


# Show columns W and X and rows A and D of the dataframe.

# In[11]:


# write your code here
rows = ['A','D']
columns = ['W', 'X']

df.loc[rows,columns]


# Define a new colum where its summation of columns W and X. Lable the new column as new.

# In[12]:


# write your code here
df['new']=df['W']+df['X']
df


# Remove the column new that you just created.

# In[18]:


# write your code here
df = df.drop(columns = ['new'])
df


# find min, max, sum,and mean of each column of the dataframe.

# In[19]:


# write your codes here
df.min(), df.sum(), df.max(), df.mean()


# find min, max, sum,and mean of each row of the dataframe.

# In[ ]:


# write your codes here
df.min(axis1), df.sum(axis1), df.max(axis1), df.mean(axis1)


# ### Extra credit
# Show only positive elements of the dataframe.

# In[31]:


# write your code here
df = df.loc[:, df.ge(0).all()]
print (df)


# In[ ]:





# ## Q2 (3 Points)

# We want to represent the students registered in BUSA 423 using a dataframe. The students registers in the course are as following. 
# 
# |   Name|    Age|     Major |     GPA|
# |----|----|----|----|
# |   Joe|     25|      MKT|       3.25|
# |   Jack  |  22   |   ACT    |   3.82|
# |   Marry  | 23 |     MGT     |  3.62|
# 
# The name of the dataframe is Students. Now, using pandas dataframe we want to create such a dataframe.

# In[33]:


import pandas as pd  # import pandas
students = pd.DataFrame (data = {'Name':['Joe','Jack','Marry'],
                                 'Age':[25,22,23],
                                 'Major': ['MKT','ACT','MGT'],
                                 'GPA': [3.25,3.85,3.62]},
                         columns = ['Name', 'Age','Major','GPA'])
print(students)


# The dean also wants to record the city that students are coming from.
#  a new column needs to be added to the current dataframe. the name of
#  the column is City. Joe is coming from Commerce, Jack and Marry both are
#  from Dallas. The following command adds the colum to the dataframe.

# In[34]:


students['city']= pd.DataFrame(['Commerce','Dallas','Dallas'])
print(students)


# Marry has informed that her GPA is incorrect and the true value is 3.75.
# we want to change her GPA to 3.75 using the following comment.

# In[35]:


students.loc[2,'GPA'] = 3.75
print(students)


# Joe suddently dropped out from school and we do not to keep his record.
# the following command deletes Joe's record.

# In[ ]:


students.drop[0]
print(students)


# ## Q3 (4 points)

# 1- Visit this website: https://www.ssa.gov/oact/babynames/limits.html
# 
# 2- download the first file, National data (7Mb)
# 
# 3- Unzip the folder and upload all the .txt files to the jupyter. Also, you can copy jupyter file into the unzipped folder.
# 
# 
# The purpose of this code is finding the top names of babys based on their gender from 1880 upto 2017.
# The function is developed based on the materials covered in the lectures. Nothing different than course materials.
# This is beauty of the python that you can do a lot of complex computation using simple codes. :-)

# In[59]:


def Top10List(Gender,n): # Define a function
    import pandas as pd # import pandas
    Name = []  # create an empty list
    Names=  {} # create an empty dictionary
    for i in range(1880,2018):  
        filename = 'yob'+str(i)+'.txt' # convert i to a datatype that can be used in open function
        with open(filename) as f:     
            text = f.read()            # read the file
            text = text.strip('\n') 
            text = text.split()
            for line in text[:1000]:            
                words = line.split(',')  # breakdown components of each line, they are seperated by ',': Name, Sex, #of Given Names
                if words[0] == Gender: # here, we check whether gender in the the above line is equal to the request Gender.
                    if words[0] in Name: # if the name is in the list of Name. 
                        Names[words[0]][i]= int(words[2]) # this line adds a key-value pair to a key in the Names dictionary
                    else:                   # otherwis conidtion
                        Name.append(words[0])  # this is a new name and its added to the Name list.
                        Names[words[0]] = {}    # in the Names dictionary, key equal to the name is created.
                        Names[words[0]][i]= int(words[2]) 
    dfNames = pd.DataFrame(Names) # converte the dictionary to a dataframe.
    dfNames = dfNames.fillna(0) # fill the NaN values with 0.
    Result = dfNames.sum() # for each column find the sum, given the column header is babyNames.
    FianlResult = Result.sort_values(ascending=False).head(n) # show the first n rows of the Result Series.  
    return FianlResult  # the missing keyword is associted with function and shows the output


# In[60]:


Top10List(n = 25, Gender = 'M') # the first call of the function:


# In[61]:


Top10List(n = 30, Gender = 'F') # the 2nd call of the function:


# In[ ]:




