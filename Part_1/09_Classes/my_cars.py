'''Importing Multiple Classes from a Module'''
# import car
# from car import Car, ElectricCar
from car import Car
from electric_car import ElectricCar

'''Importing an Entire Module'''


my_bettle = Car('volkswagen', 'bettle', 2020)
# my_bettle = car.Car('volkswagen', 'bettle', 2020)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2020)
# my_tesla = car.ElectricCar('tesla', 'roadster', 2020)
print(my_tesla.get_descriptive_name())
