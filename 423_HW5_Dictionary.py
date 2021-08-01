#!/usr/bin/env python
# coding: utf-8

# ## Q1 (2 Points)

# Consider the following variable.

# In[1]:


myvar = { 1:{'name': 'joe', 'age' : 20}, 2:{'name': 'john', 'age' : 30}}


# In[2]:


#1.1: What is the type of this variable.
print(type(myvar)) 


# In[3]:


#1.2: We want to show joe as the result of the following code,
# complete the following command such that it shows joe.
print(myvar [1]['name'])


# In[10]:


#1.3: We want to add a new element to this variabe,
#the person that we want to add is Mike, 25 years old.
# complete the following commands. 
myvar[3] = {} 
myvar[3]['name'] = 'Mike'
myvar[3]['age'] = 25 

print(myvar)


# In[2]:


#1.4 Now, we want to find the average of ages.
# complete the following commands.

x = 0 
for var1 in myvar.keys():
    x += myvar[var1]['age']
mean = x/len(myvar)
print(mean)


# ## Q2. (2 points)

# Considere the following variable.

# In[4]:


Students_Info={'lloyd' : {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
},
'alice':{
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
},
'tyler': {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}}


# In[7]:


# 2.1. Show Lloyd's all info
print(Students_Info['lloyd'])


# In[8]:


# 2.2. Show Lloyd's Homework grades
print(Students_Info['lloyd']['homework'])


# In[9]:


# 2.3. Show Lloyd's last grade on the homework.
print(Students_Info['lloyd']['homework'][3])


# In[5]:


# 2.4. Show Lloyd's average on homework if all of them have the same percentages.
print(sum(Students_Info['lloyd']['homework'])/len(Students_Info['lloyd']['homework']))


# ## Q3 (2 points)

# Create a function space_lower_upper_count that accepts a string and returns a dictionary that contains the count for spaces, upper and lower case characters in that string. For example “Texas State” should get {‘spaces’:1,’lower’: 8, ‘upper’: 2}.

# In[6]:


word = 'Texas State'
d= {'UPPER_CASE':0, 'LOWER_CASE':0,'SPACE':0}

for characters in word:
    if characters.isupper():
        d['UPPER_CASE']+=1
    elif characters.islower():
        d['LOWER_CASE']+=1
    else:
        d['SPACE']+=1
print(d)


# In[5]:





# ## Q4. (2 points)

# In[13]:


# run this code first
get_ipython().system('pip3 install COVID19Py')


# In[6]:


# run this code as well.
import COVID19Py
covid19 = COVID19Py.COVID19()
location = covid19.getLocationByCountryCode("US")
print(location)


# Based on the above data, find covid-19 infection rate and death rate? 

# In[7]:


# infection rate:

location[0]['latest']['confirmed']/location[0]['country_population']


# In[8]:


# death rate

100*location[0]['latest']['deaths']/location[0]['country_population']


# ## Q5 (2 points)

# Consider the following text. Find the frequency of the words in this text.

# In[39]:


str1= """
The Master of Science in Business Analytics is an approved Science,
Technology, Engineering and Mathematics (STEM) program.
The program offers students from business and non-business 
backgrounds an opportunity to develop expertise in the art 
and science of business analytics in this high-demand field. 
Students will learn how to collect, organize, analyze, optimize and 
interpret Big Data. The program emphasizes decision-making 
skills to apply Big Data findings to business challenges.
Our faculty have been involved in research on social media, 
organization behavior analytics, service computing, business analytics, 
reliable distributed systems, web databases and semantic integration systems.
Learn statistical and research methods.
Acquire knowledge in database management and data warehousing.
Identify, document, model, assess and improve core business processes.
Appreciate relevant business trends in the marketplace and consumer behaviors.
Develop skills that prepare you for the demands of the global business environment.
Enhance your project management skills including initiation, planning, execution, controlling and closing projects.
Investigate the technologies, methods and practices that foster innovation,
new business opportunities and new efficiencies.
"""


# In[41]:





# In[37]:


str1 = str1.split(' ')
d = dict()

for word in str1:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
print(d)


# In[ ]:




