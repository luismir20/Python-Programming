#!/usr/bin/env python
# coding: utf-8

# ## Q1. Numpy Basics (5 points)

# 1.a. Import the numpy package under the name np
# 

# In[1]:


import numpy as np


# 1.b. Create a null (zeros) vector of size 10

# In[22]:


np.zeros(10)


# 1.c. Create a vector with values ranging from 10 to 50 and then convert it  into $10\times 4 $ matrix. 

# In[6]:


a = np.random.randint(10,50,(10,4))


# 1.d. show the second column of the previous section (i.e., `1.c.`)

# In[8]:


a[:,1]


# 1.e. show the second row of 1.c.

# In[7]:


a[1,:]


# 1.f. Create a 3x3 array with random values

# In[54]:


f = np.random.normal(5,2,(3*3))
f


# 1.g.Create another 3x3 array with random values and add it to the matrix of the question `1.f`

# In[56]:


f+np.random.normal(3,3,(3*3))


# 1.h. create 10 random numbers from standard Normal distribution ( mean = 0, sigma = 1).

# In[11]:


b = np.random.normal(0,1,10)


# 1.i. find `mean`,`median`,`sum`,and `standard deviation` of the priveious quesiont (`1.h`).

# In[30]:


np.mean(b), np.sum(b), np.median(b), np.std(b)


# ## Q2. (5 points)

# In[34]:


A = np.arange(1,26).reshape(5,5)
A


# In[15]:


A[2:,1:]


# In[13]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[37]:


A[3][4]


# In[14]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[47]:


A[:3,1:2]


# In[16]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# Get the sum of all the values in the matrix `A`

# In[31]:


np.sum(A)


# Get the standard deviation of the values in the matrix `A`

# In[32]:


np.std(A)


# Get the sum of all the columns in the matrix `A`.

# In[51]:


np.sum(A[:4,:])


# Get the sum of all the rows in the matrix `A`.

# In[50]:


np.sum(A[:,:4])


# ## Extra Credit.  (2 points)

# `numpy` can be used to solve linear equations $AX=B$ where $A$,$B$ and $X$ are matrices. Check the detail from here: https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve

# Consider the following equations.
# \begin{align}
# 2X+3Y= 5 \\
# 3X-2Y= 2
# \end{align}
# 
# find $X$ and $Y$ that satisfy the above equations.

# In[ ]:




