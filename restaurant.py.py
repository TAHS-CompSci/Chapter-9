#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Restaurant():   
        
    def __init__(self, resturant_name, cuisine_type): 
        self.name = resturant_name        
        self.menu = cuisine_type  
        self.served= 0
        
    def read_served(self):              
        print("This Restaurant Has Served " + str(self.served) + " People!")    
    
    def update_served(self, served): 
        if served >= self.served:
            self.serve = served
        else:
            print("No One Has Been Surved")
            
    def increment_served(self, surved):  
        self.served += surved
    
    def open(self):       
        print(self.name.title() + " is now open.")
        
Huberta = Restaurant(' Huberta', 'Onion',)

print("We Are Called"  +  Huberta.name.title() + ".") 
print("Our Menu has " + str(Huberta.menu) + ".")

Huberta.update_served(48)


Huberta.increment_served(19) 

