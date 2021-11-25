class Dog:
    """A simple attemp to model a dog"""

    def __init__(self, name, age):
        """Initialize the name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in resposne to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rollling over in response to command."""
        print(f"{self.name} rolled over!")


'''Making an Instance from a Class'''
my_dog = Dog('Neptune', 1)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

'''Accessing Attributes'''
# my_dog.name

'''Calling Methods'''
# my_dog.sit()
# my_dog.roll_over()

'''Creating Multiple Instances'''
my_dog1 = Dog('Butch', 12)
my_dog2 = Dog('Coco', 10)

# print(f"My dog's name is {my_dog1.name}.")
# print(f"My dog is {my_dog1.age} years old")
# my_dog1.sit()

# print(f"My dog's name is {my_dog2.name}.")
# print(f"My dog is {my_dog2.age} years old")
# my_dog2.sit()
