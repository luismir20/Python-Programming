#!/usr/bin/env python
# coding: utf-8

# ## Q1. (2 points)

# Write the following statement using while loop.

# In[1]:


for i in range(10):
    print(i)


# In[5]:


# write your code here:
i=0
while (i<10):
    print(i)
    i=i+1 


# ## Q2. (2 points)

# Using a while loop, create a list numbers that contains the numbers 0 through 35. Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1. The while loop should stop when the counter is greater than 35.

# In[16]:


# write your code here:

lst=[]
counter=0
while (counter<36):
    lst.append(counter)
    counter+=1
print(lst)


# ## Q3. (2 points)

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# 
# Note : Use `continue` statement.
# 
# Expected Output : 0 1 2 4 5

# In[27]:


# write your code here:
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")


# ## Q4. (2 points)

# Write a program that iterates through the list and check whether 100 is in the list or not, if 100 is in the list, it prints it with its index number. i.e.: "There is a 100 at index no: 5"

# In[35]:


# write your code here and test it on the following list

lst=[10,99,98,85,45,59,65,66,76,12,35,13,100,80,95]
print('There is a 100 at index no:',lst.index(100))





# ## Q5. (2 points)

# Write a program to calculate factorial of a number. Factorial of any number n is represented by $n!$ and is equal to $1\times2\times3\times \dots \times(n-1)\times n$. For instance, $4! = 1 \times 2 \times3 \times4 = 24. $
# Also,
# 1! = 1 and
# 0! = 1

# In[40]:


# write your code.
x = int(input())  # this is the number entered by the user.

factorial=1
x=int(input())
if x==1:
    print(1)
elif x==0:
    print(1)
else:
    for i in range(1,x + 1):
        factorial = factorial*i
    print("The factorial of",x,"is",factorial)


# In[ ]:




