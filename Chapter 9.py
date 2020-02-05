#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import OrderedDict

"""
Program Name: OrderedDict Rewrite.py
Programmer Name: Adam Elkins
Description: a rewirte of a dictionary of key terms of programning 
"""
glossary = OrderedDict()

glossary['string'] = 'A series of characters'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = 'a collection of key-value pairs.'
glossary['key'] = 'The first item in a key-value pair dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A test to see a comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates either True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)


# In[ ]:





# In[ ]:




