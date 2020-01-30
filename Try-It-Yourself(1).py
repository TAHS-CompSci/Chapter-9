#!/usr/bin/env python
# coding: utf-8

# In[12]:


#9-1 Resturant
'''
Programmer: Drayzdin Thompson
Description: Creat a class called resturant
'''
class Resturant():
    def __init__(self, resturant_name, resturant_type):
        self.resturant_name = resturant_name
        self.resturant_type = resturant_type
    def describe_resturant(self):
        print("welcome to " + self.resturant_name.title() + ".")
        print("We are a " + self.resturant_type.title() + " Resturant.")
    def open_resturant(self):
        print(self.resturant_name + " is now open.")

my_resturant = Resturant("Pizza for Days", "Fast Food")
print(my_resturant.resturant_name.title() + " is the name of my resturant.")
print(my_resturant.resturant_type.title() + " is the way.")
my_resturant.describe_resturant()
my_resturant.open_resturant()


# In[13]:


#9-2 Three Resturants
'''
Programmer: Drayzdin Thompson
Description: Call Class above three times 
'''
first_resturant = Resturant('Yumzzz Fries', 'Buffet')
second_resturant = Resturant('I Scream for Ice only', 'Fast Food')
third_resturant = Resturant('Bergsi', 'Fast Food')
first_resturant.describe_resturant()
second_resturant.describe_resturant()
third_resturant.describe_resturant()


# In[23]:


#9-3 Users
'''
Programmer: Drayzdin Thompson
Description: New Class defining a user
'''
class User():
    def __init__(self, first_name, last_name, password, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.gender = gender
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ' is ' + self.gender.title())
        print('password = '+  self.password)
        print('Username = ' + self.username)
    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + " thank you for visiting.")
drayzdin = User('Drayzdin', 'Thompson', 'Aberration11', 'Drayzdin02', 'Male')
drayzdin.describe_user()
drayzdin.greet_user()


# In[12]:


#9-4 Number served
'''
Programmer: Drayzdin Thompson
Description: Adding more functions to the class resturant
'''
class Resturant():
    def __init__(self, resturant_name, resturant_type):
        self.resturant_name = resturant_name
        self.resturant_type = resturant_type
        self.number_served = 0
    def describe_resturant(self):
        print("welcome to " + self.resturant_name.title() + ".")
        print("We are a " + self.resturant_type.title() + " Resturant.")
    def open_resturant(self):
        print(self.resturant_name + " is now open.")
    def set_number_served(self, served_count):
        self.number_served = served_count
    def increment_number_served(self, raise_count):
        self.number_served += raise_count
        
resturant = Resturant('Dray', "buffet")
print(resturant.number_served)
resturant.set_number_served(20)
print(resturant.number_served)
resturant.increment_number_served(20)
print(resturant.number_served)


# In[25]:


#9-5 Login Attempts
'''
Programmer: Drayzdin Thompson
Description: More Functions for class user
'''
class User():
    def __init__(self, first_name, last_name, password, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ' is ' + self.gender.title())
        print('password = '+  self.password)
        print('Username = ' + self.username)
    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + " thank you for visiting.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
drayzdin = User('Drayzdin', 'Thompson', 'Aberration11', 'Drayzdin02', 'Male')
print(drayzdin.login_attempts)
drayzdin.increment_login_attempts()
print(drayzdin.login_attempts)
drayzdin.reset_login_attempts()
print(drayzdin.login_attempts)
print()
kellen = User('kellen', 'barron', 'stuff', 'more_stuff', 'male')
print(kellen.login_attempts)
kellen.increment_login_attempts()
print(kellen.login_attempts)
kellen.increment_login_attempts()
print(kellen.login_attempts)
kellen.increment_login_attempts()
print(kellen.login_attempts)
kellen.increment_login_attempts()
print(kellen.login_attempts)
kellen.reset_login_attempts()
print(kellen.login_attempts)


# In[19]:


#9-6 ice cream stand
'''
Programmer: Drayzdin Thompson
Description: Write a child class 
'''
class Resturant():
    def __init__(self, resturant_name, resturant_type):
        self.resturant_name = resturant_name
        self.resturant_type = resturant_type
        self.number_served = 0
    def describe_resturant(self):
        print("welcome to " + self.resturant_name.title() + ".")
        print("We are a " + self.resturant_type.title() + " Resturant.")
    def open_resturant(self):
        print(self.resturant_name + " is now open.")
    def set_number_served(self, served_count):
        self.number_served = served_count
    def increment_number_served(self, raise_count):
        self.number_served += raise_count

class IceCreamStand(Resturant):
    def __init__(self,resturant_name,resturant_type):
        super().__init__(resturant_name, resturant_type)
        flavor = ['vanilla','chocolate','mint','neopolitan']
        self.flavor = flavor
    def describe_flavors(self):
        print(str(self.flavor))
chips_ahoy = IceCreamStand('Chips Ahoy', 'ice cream stand')
chips_ahoy.describe_flavors()


# In[20]:


#9-7 Admin
'''
Programmer: Drayzdin Thompson
Description: Child class work
'''
class User():
    def __init__(self, first_name, last_name, password, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ' is ' + self.gender.title())
        print('password = '+  self.password)
        print('Username = ' + self.username)
    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + " thank you for visiting.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    def __init__(self, first_name, last_name, password, username, gender):
        super().__init__(first_name, last_name, password, username, gender)
        priviliges = ['can add post', 'can delete post', 'can ban user', 'can un-ban user']
    def show_priviliges(self):
        print(str(self.priviliges))
administrator = Admin('Drayzdin', 'Thompson', 'Aberr1', 'Dray02', 'Male')
administrator.show_priviliges()


# In[21]:


#9-8 priviliges
'''
Programmer: Drayzdin Thompson
Description: More child work as well as class within a class
'''
class User():
    def __init__(self, first_name, last_name, password, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.gender = gender
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ' is ' + self.gender.title())
        print('password = '+  self.password)
        print('Username = ' + self.username)
    def greet_user(self):
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + " thank you for visiting.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
class Admin(User):
    def __init__(self, first_name, last_name, password, username, gender):
        super().__init__(first_name, last_name, password, username, gender)
        priviliges = ['can add post', 'can delete post', 'can ban user', 'can un-ban user']
        self.priviliges = Priviliges()

class Priviliges():
    def __init__(self, priviliges = ['can add post', 'can delete post', 'can ban user', 'can un-ban user']):
        self.priviliges = priviliges
    def show_priviliges(self):
        print(str(self.priviliges))
administrator = Admin('Drayzdin', 'Thompson', 'Aberr1', 'Dray02', 'Male')
administrator.priviliges.show_priviliges()


# In[25]:


#9-9 Battery upgrade
'''
Programmer: Drayzdin Thompson
Description: Reveiwing classes
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print('This car does not need gas')

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
         print("This car has a " + str(self.battery_size) + " -kwh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif  self.battery_size == 85:
            range = 270
        print("This car can go approximatly " + str(range) + " miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

my_testla = ElectricCar('testla','model s','2016')
my_testla.battery.get_range()
my_testla.battery.upgrade_battery()
my_testla.battery.get_range()


# In[3]:


#9-10 imported resturant
'''
Programmer: Drayzdin Thompson
Description: Import work, does it work 
'''
from resturant import Resturant

my_rest = Resturant('dr.food','buffet')
my_rest.describe_resturant()


# In[10]:


#9-11 imported admin
'''
Programmer: Drayzdin Thompson
Description: show how import works 
'''
from user import Admin

admin = Admin('Drayzdin', 'Thompson', 'Aberr1', 'Dray02', 'Male')
admin.priviliges.show_priviliges()


# In[26]:


#9-12  multiple modules
'''
Programmer: Drayzdin Thompson
Description: import function through multiple files
'''
from user import User
from admin import Admin

drayzdin = Admin('Drayzdin', 'Thompson', 'Aberration11', 'Drayzdin02', 'Male')
admin.priviliges.show_priviliges()


# In[36]:


#9-14 Dice  
'''
Programmer: Drayzdin Thompson
Description: make a dice class for games 
'''
import random

class Die():
    import random
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        die_roll = random.randint(1, self.sides)
        print(die_roll)

six_die = Die(6)
for roll in range(10):
    six_die.roll_die()

six_die = Die(10)
for roll in range(10):
    six_die.roll_die()

six_die = Die(20)
for roll in range(10):
    six_die.roll_die()
    

