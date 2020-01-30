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