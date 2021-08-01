#!/usr/bin/env python
# coding: utf-8

# # HW1 of BUSA 423

# The purpose of this assignment is working with `Jupyter Notebook` and `print` function.
# 
# Please write your answers in the file and then download `ipynb` file and turn it into `D2L`.

# ## Q1. Introduce yourself (3 Points)

# Write a code that prints the following statement. Replace `[]` with your info.
# 
# `Hello. My name is [Your_Name], and my major is [Your Major]. Nice to meet you!`

# In[5]:


print("Hello. My name is Luis, and my major is business analytics. Nice to meet you!")


# ## Q2. (3 points)

# Write a program that shows `Hello World!` on the screen, followed by an empty line and then `Welcome to Python` on the third line.

# In[4]:


print("Hello World!")
print("")
print("Welcome to Python")


# ## Q3. (2 Points)

# Write a program that shows `4 * 5` is equal to `20`.

# In[6]:


print('4*5', 'is equal to', 4*5)


# ## Q4. (2 Points)

# `help function` of Python is very helpful. To use this function, just type `help(Function_name)`.
# 
# Use the `help function` on print and see the output.

# In[2]:


help(print)


# Based on the output of the help function, by default, the seperator of elements in the `print` function is a space character, `sep=' '`. It can be replaced by other characters as well, for instance, `sep=', '`, that is, elements are sepreated by a comma. In the following cell, instead of `?` put `sep=', '` and compare the outcome of two statements. 

# In[1]:


print('Hello', 'How are you?')
print('Hello', 'How are you?', sep=', ')

