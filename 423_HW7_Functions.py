#!/usr/bin/env python
# coding: utf-8

# ## Q1. (2 points)

# Joe wants to write a code to compute the perimeter of a rectangle. The following is his code which has four errors. Fix the errors. 

# In[2]:


def rec_perimeter(length, width):
    perimeter = 2* (length + width)
    return perimeter

print(rec_perimeter(10,5))


# call the function for a rectangle with length = 10 ft and width = 5 ft. 

# ## Q2. (2 points)

# Write a function that counts the number of even numbers when a list of integer is passed in. Fill ____ pieces of the following function.
# 

# In[31]:


def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num %2 == 0:
            count += 1 
    return count

count_even_numbers([1,2,3,4])


# ## Q3 (2 points)

# We want to write a function to find the harmonic mean.
# More detail can be found here: https://en.wikipedia.org/wiki/Harmonic_mean
# 
# Assume that we want to pass unknow number of arguments represented by vars to the function

# In[24]:


def HarmonicMean(*vars): #(2 points(
    x = 0
    for var in vars:
        x += 1/var
    return len(vars)/x
# now we want to test the code for numbers from 1 to  10 (included).
vars = list(range(1,11)) # 1 point
print(HarmonicMean(*vars))


# ## Q4 (2 points)

# Write a function that will return the number of digits in an integer.

# In[32]:


# write your code here:
def number_of_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

print(number_of_digits(150))


# ## Q5. (2 points)

# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29.

# In[30]:


def sum_of_squares(xs):
    sum=0
    for num in xs:
        sum = sum + (num*num)
    return sum

print(sum_of_squares([2,3,4]))


# In[ ]:




