#!/usr/bin/env python
# coding: utf-8

# Chapter 9 Hoffman Proggramer: Tobin Hoffman Notes for Chapter 9 class

# In[1]:


class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """"Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# In[2]:




    
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


# In[3]:


my_dog.name


# In[4]:


my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()


# In[5]:


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


# In[6]:


class Restaurant():
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    def describe_restaurant(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is a pizirea.")
    def open_restaurant(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " is now open!")
    


# In[7]:


my_restaurant = Restaurant('pizza hut', 'pizza')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# In[8]:


my_restaurant = Restaurant('pizza hut','pizza')
print("My restaurants name is " + my_restaurant.name.title() + ".")
print("My restaurants cuisine is " + (my_restaurant.cuisine))


# In[9]:


my_restaurant = Restaurant('KFC','chicken')
print("My restaurants name is " + my_restaurant.name.title() + ".")
print("My restaurants cuisine is " + (my_restaurant.cuisine))


# In[10]:


my_restaurant = Restaurant('MCdonalds','fast food')
print("My restaurants name is " + my_restaurant.name.title() + ".")
print("My restaurants cuisine is " + (my_restaurant.cuisine))


# In[11]:


class User() :
    def __init__(self, name, last, info):
        self.name = name
        self.last = last
        self.info = info
    def user_info(self):
        print("First Name:" + self.name.title())
        print("Last Name:" + self.last.title())
        print("Summary:" + self.info.title())
    


# In[12]:


my_user = User('tobin', 'hoffman', 'likes to play soccer')


# In[13]:


my_user.user_info()


# In[14]:


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
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
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


# In[15]:


class Restaurant():
    def __init__(self,name,cuisine,number):
        self.name=name
        self.cuisine=cuisine
        self.number=number
    def describe_restaurant(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is a pizirea.")
    def open_restaurant(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " is now open!")
    


# In[16]:


my_restaurant = Restaurant('KFC','chicken','69')
print("My restaurants name is " + my_restaurant.name.title() + ".")
print("My restaurants cuisine is " + (my_restaurant.cuisine))
print("My restaurants has served " + (my_restaurant.number)+" people.")


# In[17]:


class User() :
    def __init__(self, name, last, info, login):
        self.name = name
        self.last = last
        self.info = info
        self.login = login
    def user_info(self):
        print("First Name:" + self.name.title())
        print("Last Name:" + self.last.title())
        print("Summary:" + self.info.title())
        login = 0
        login+=1
    def increment_login_attempts(self):
        print ('log attempts: '+ self.login())
    


# In[18]:


my_user = User('tobin', 'hoffman', 'likes to play soccer', '0')


# In[19]:


my_user.user_info()


# In[20]:


class Car():
    """A simple attempt to represent a car."""
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
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
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
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        """Initialize attributes of the parent class."""
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[21]:


my_tesla.battery.describe_battery()


# In[22]:


class Ice():
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    def describe_icet(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is a Ice cream stand.")
    def open_ice(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " is now open!")
    def menu(self) :
        print ('Flavors:')
        print('strawberry')
        print('chocolate')
        print('Vanilla')
        print('cotton candy')
        print('mango')
        print('rainbow sherbert')
    


# In[23]:


my_ice = Ice('ice cream stand', 'ice cream')
print("My restaurants name is " + my_ice.name.title() + ".")
print(my_ice.menu())


# In[ ]:





# In[24]:


class User() :
    def __init__(self, name, last, info, status):
        self.name = name
        self.last = last
        self.info = info
        self.status = status
    def user_info(self):
        print("First Name:" + self.name.title())
        print("Last Name:" + self.last.title())
        print("Summary:" + self.info.title())
        login = 0
        login+=1
    def privaliges(self):
        if self.status.title =='admin':
            print('admin')
            print('Can add post')
            print('Can delete post')
            print('can edit post')
            print('can ban user')
        
    


# In[25]:


my_user = User('tobin', 'hoffman', 'likes to play soccer', 'admin')


# In[26]:


my_user.user_info()


# In[27]:


class Car():
    """A simple attempt to represent a car."""
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
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
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
            self.battery_size = 85
            print ('If you battery gets upgraded to aa 85-KWH battery, it could go 270 miles on a full charge.')
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        """Initialize attributes of the parent class."""
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[28]:


from car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# In[29]:


from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[30]:


from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[31]:


import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[33]:


from car import Car
from car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())


# In[34]:


from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# In[38]:


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




