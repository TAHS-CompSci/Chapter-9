#!/usr/bin/env python
# coding: utf-8

# Ch 9 Walz
# Programmer:Gavin Walz
# Notes for Ch 9

# In[6]:


class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# In[7]:


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


# In[8]:


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


# In[9]:


class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(self.name.title() + " is a restaurant.")
    def open_restaurant(self):
        print(self.name.title() + " is open now!")


# In[10]:


my_restaurant = Restaurant('pizza hut','pizza')
print('My restaurant name is '+ my_restaurant.name.title()+'.')
print('My restaurant cuisine is '+ (my_restaurant.cuisine))


# In[11]:


my_restaurant = Restaurant('KFC','chicken')
print('My restaurant name is '+ my_restaurant.name.title()+'.')
print('My restaurant cuisine is '+ (my_restaurant.cuisine))


# In[12]:


my_restaurant = Restaurant('McDonalds','Fast food')
print('My restaurant name is '+ my_restaurant.name.title()+'.')
print('My restaurant cuisine is '+ (my_restaurant.cuisine))


# In[13]:


class User():
    def __init__(self, name, last, info):
        self.name = name
        self.last = last
        self.info = info
    def user_info(self):
        print('First name: ' + self.name.title())
        print('Last name: ' + self.last.title())
        print('Summary: ' + self.info.title())


# In[14]:


my_user = User('Gavin', 'Walz', 'Plays on computer')


# In[15]:


my_user.user_info()


# In[16]:


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# In[17]:


class Restaurant():
    def __init__(self, name, cuisine,number):
        self.name = name
        self.cuisine = cuisine
        self.number=number
    def describe_restaurant(self):
        print(self.name.title() + " is a restaurant.")
    def open_restaurant(self):
        print(self.name.title() + " is open now!")


# In[18]:


my_restaurant = Restaurant('pizza hut','pizza','45')
print('My restaurant name is '+ my_restaurant.name.title()+'.')
print('My restaurant cuisine is '+ (my_restaurant.cuisine))
print('My restaurant has served '+ (my_restaurant.number)+' people.')


# In[19]:


class User():
    def __init__(self, name, last, info):
        self.name = name
        self.last = last
        self.info = info
    def user_info(self):
        print('First name: ' + self.name.title())
        print('Last name: ' + self.last.title())
        print('Summary: ' + self.info.title())
    def increment_login_attempts(self):
        print('Login attempts: '+ login)


# In[20]:


my_user = User('Gavin', 'Walz', 'Plays on computer')


# In[21]:


my_user.user_info()


# In[22]:


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[23]:


my_tesla.battery.describe_battery()


# In[24]:


class Ice():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(self.name.title() + " is a restaurant.")
    def menu(self):
        print('Flavors: ')
        print('Strawberry')
        print('Chocolate')
        print('Vanilla')


# In[25]:


my_ice = Ice('Ice Land','Ice Cream')
print('My restaurant name is '+ my_ice.name.title()+'.')
print(my_ice.menu())


# In[26]:


class Admin():
    def __init__(self, name, last, info, status):
        self.name = name
        self.last = last 
        self.info = info
        self.status = status
    def user_info(self):
        print('First name: ' + self.name.title())
        print('Last name: ' + self.last.title())
        print('Summary: ' + self.info.title())
    def privaliges(self):
        if self.status.title=='admin':
            print('Admin')
            print('Can add post')
            print('Can delete post')
            print('Can ban user')
        


# In[27]:


my_admin = Admin('Gavin', 'Walz', 'Plays on computer', 'admin')


# In[28]:


my_user.user_info()


# In[29]:


my_admin.privaliges()


# In[30]:


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        if self.battery_size == 70:
                self.battery_size =  85
                print('If your battery gets upgraded to a 85-kWh battery, it could go 270 miles on a full charge.')

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[31]:


from car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# In[32]:


from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[33]:


from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[34]:


import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[35]:


from car import Car
from car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[37]:


from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# In[39]:


from random import randint

class Die():

    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)


# In[ ]:





# In[ ]:




