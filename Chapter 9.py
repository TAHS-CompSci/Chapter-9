#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = 'joe'
        self.age = 4
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
        
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")


# In[20]:


my_dog.name


# In[3]:


print("My dog is " + str(my_dog.age) + " years old.")


# In[2]:


from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collectionof items, one at a time.'
glossary['dictionary'] = 'a collection of key-value pairs.'
glossary['key'] = 'The first item in a key-value pair dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value witha decimal component.'
glossary['boolean expression'] = 'An expression that evvaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)


# In[ ]:




