"""A class that can be used to represent a car."""
"""A set of classes used to represent gas and electric cars."""


class Car:
    """A simple attempt to repsesent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # 1.Setting a Default value for an Attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        # 1.Setting a Default value for an Attribute
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        # 2.Modifying an Attribute's Value Through a Method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the gien amount to the odometer reading."""
        # 3.Incrementing an Attribute's Value Through a Method
        self.odometer_reading += miles


'''The __init__() Method for a child Class'''
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
'''Defining Attributes and Methods for the Child Class'''
# my_tesla.describe_battery()
'''Instance as Attributes'''
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# 1.Setting a Default value for an Attribute
# my_new_car.read_odometer()

"""Modifying Attribute Values"""
# 2.Modifying an Attributes Value Directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

"""2.Modifying an Attribute's Value Through a Method"""
# my_new_car.update_odometer(22)
# my_new_car.read_odometer()

"""Incrementing an Attribute's Value Through a Method"""
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
