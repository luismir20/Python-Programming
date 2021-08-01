#!/usr/bin/env python
# coding: utf-8

# ## Q1. (5 Points)

# We want to creat a class Player with attributes name and age. Then we want to creat a subclass of Player called defender,
#  at the end, we creat an object from each classes. 

# In[6]:


class Player(): #create the class Player
    
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def ShowInfo (self): # we creat a method here
        print(self._name + ' is '+ str(self._age) + ' old')

class Defender(Player):#create the class Defender as a subclass of the class Player
    def __init__(self,name,age):
        Player.__init__(self,name,age)
        self._income = 10000

    def ShowInfo (self): # we creat a method here
        print(self._name + ' is '+ str(self._age) + ' old ' + 'with ' + str(self._income) + ' income')
    
        
player1 = Player('John',25) # player1 is an instance of the Class Player
player1.ShowInfo() # call the showinfo function for player1
Player2 = Defender('Joe',27)# player2 is an instance of the Class Defender
Player2.ShowInfo()# call the showinfo function for player2


# ## Q2. (5 Points)

# Create a Vehicle class with max_speed and mileage instance attributes.

# In[38]:


# write your code here.
class Vehicle():
    def __init__ (self, make, year, max_speed, mileage):
        self.make = make
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
    def get_descriptive_name(self):
        long_name = str(self.make)+ ' ' +'is year '+ str(self.year)+ ' ' + 'has ' + str(self.max_speed)+ ' ' + 'max speed and ' + str(self.mileage)
        return long_name.title()
vehicle1 = Vehicle('BMW', 2020, 250, '20 mpg')
print(vehicle1.get_descriptive_name())


# In[39]:


# class your class with max_speed= 250 and milage = 20.
vehicle1 = Vehicle('BMW', 2020, 250, '20 mpg')
print(vehicle1.get_descriptive_name())


# Now, create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# In[40]:


# Write your code here.
class Bus(Vehicle):
    pass

school_bus = Bus('School Mercedes',2020, 400, '15 mpg')
print(school_bus.get_descriptive_name())


# In[ ]:




