#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class OrderedDict():

     def __init__(self, name, definition):
            self.nam = name
            self.defi = defintion
            

    
Definitions = {
    'Dictionary': 'Dictionaty: dictionary is wrapped in braces, {}, with a series of keyvalue pairs inside the braces',
    'Value': 'Value: A word/term asssoicated with a function/key',
    'In-Put': 'In-Put: What the user/programer puts in that gets manipulated/changed from the code',
    'Out-put' : 'Out-Put: What the user/progermer gets from a coding program',
    'key': 'Key: Each key is connected to a value, and you can use a key to access the value associated with that key. ',
    'loop':'loop: repets a string of code till told other wise',
    'indentation' : 'Indentation: the nessiaary spacing between code for tree based structures',
    'set':'Set: warps around a group of items & dupiliates them',
    'python' : 'Python: A type of coding language that has many versions, its current version is 3',
    'jupyter' : 'Jupyter Notebook: A program that places coding into itself & can be exported', }

for name in (Definitions.keys()): 
        print(Definitions[name].title() + "!")
Dictionaty: Dictionary Is Wrapped In Braces, {}, With A Series Of Keyvalue Pairs Inside The Braces!
Value: A Word/Term Asssoicated With A Function/Key!
In-Put: What The User/Programer Puts In That Gets Manipulated/Changed From The Code!
Out-Put: What The User/Progermer Gets From A Coding Program!
Key: Each Key Is Connected To A Value, And You Can Use A Key To Access The Value Associated With That Key. !
Loop: Repets A String Of Code Till Told Other Wise!
Indentation: The Nessiaary Spacing Between Code For Tree Based Structures!
Set: Warps Around A Group Of Items & Dupiliates Them!
Python: A Type Of Coding Language That Has Many Versions, Its Current Version Is 3!
Jupyter Notebook: A Program That Places Coding Into Itself & Can Be Exported!

