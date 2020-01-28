#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User():
    
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name
        self.attempts = 0
    def describe_self(self):
        print(self.fn.title() + self.ln.title() + "is a user of this site!")
    
    def greet_user(self):
        print("Thanks For Coming" + self.fn.title() + self.ln.title() + '!') 
        
    def login_attempts(self, attempts):
        if attempts >= self.attempts:
            self.attempts = +1
        else:
            self.attempts = 0

class Admin():

    def __init__(self, show_privliages):
        self.pri = show_priviliages
        
Privliages = {
    'can ban user'
    'can delete posts'
}

class Mod():
    def __init__(self, show_privliage):
        self.pri = show_priviliage
        
priviliage = {
    'can delete posts'
    'can mute'
}


# In[ ]:




