#!/usr/bin/env python
# coding: utf-8

# # BUSA423.HW3:Lists

# The purpose of this assignment is working on the list.

# ## Q1.  (2 points) 

# Fill the ____ parts of the code below.

# In[5]:


# Let's create an empty list
my_list = []

# Let's add some values
my_list.append('Python')
my_list.append('is ok')
my_list.append('sometimes')

# Let's remove 'sometimes'
my_list.remove('sometimes')

# Let's change the second item
my_list[1] = 'is neat'

print(my_list)


# In[ ]:





# ## Q2. (2 points)

# Consider the following list. Write a program to find total and mean of the list.

# In[42]:


list1 = [ i for i in range(1000) if i%3 ==0]


# In[44]:


result = 0.0
mean = 0.0
for i in list1:
    result = result + i
mean = result/len(list1)
print(result)    
print(mean)



# ## Q3: (2 points)

# Consider the following list. Write a program that stores the reverse of `NumberList` in a new list called `NumberListRevised`. 
# 
# Hint. Start with the empty list `NumberListRevised` and fill it using the `pop()` function on `NumberList` multiple times.

# In[38]:


NumberList = [i for i in range(11)]


# In[39]:


# write your program here:
NumberListRevised=[]

NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))
NumberListRevised.append(NumberList.pop(-1))


print(NumberListRevised)


# In[ ]:





# ## Q4: (4 points)

# Consider the following list.

# In[40]:


ListofNums = [[0],[1,2,3],[4,5,6,7],[8,9,10]]


# In[8]:


#4.1: Using list indices print the first, then the second and then the third child list.
ListofNums[0:3]


# In[10]:


# 4.2: Using list indices, print out elements 0,3,4,9
print(ListofNums[0][0])
print(ListofNums[1][2])
print(ListofNums[2][0])
print(ListofNums[3][1])


# In[11]:


# 4.3. Replace the object 8 with 88.
ListofNums [3][0]=88
print(ListofNums)


# In[12]:


# 4.4. Append the new child list [11,12,13,14] to the end of the nested list.

ListofNums.append([11,12,13,14])
print(ListofNums)


# In[14]:


# 4.5. Using del function, remove the second child list in the nested list

del ListofNums[1]
print(ListofNums)


# In[32]:


#4.6. Using the remove() function, remoce the elements 4 and 9 rom the nested list
ListofNums = [[0],[1,2,3],[4,5,6,7],[8,9,10]]
ListofNums[2].remove(4)
ListofNums[3].remove(9)
print(ListofNums)


# In[36]:


#4.7. Usingh the in function, check whether the numnber 10 is in any of the child list
for x in ListofNums:
    if 10 in x:
        print('Yes')
        

        


# In[42]:


# 4.8. Using the len() function, determin how many child list are containted in the parent list
print(len(ListofNums))


# In[ ]:




