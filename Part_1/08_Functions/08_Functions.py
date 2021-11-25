# ============================================================================================================
'''Chapter 8 Functions// Pg.129'''
# ============================================================================================================
"""Functions are blocks of code that are designed to do one specific job"""

# ============================================================================================================
'''Defining a Functions'''
# ============================================================================================================

# greeter.py




from pizza import *
import pizza as p
from pizza import make_pizza as mp
from pizza import make_pizza, function_2
import pizza
def greet_user_01():
    """Display a sime greeting."""
    print("Hello")


# greet_user_01()

def greet_user_02(username):
    """Passing Information to a Function"""
    print(f"Hello, {username.title()}")


# greet_user_02('jovan')

# ============================================================================================================
'''Passing Arguments'''
# ============================================================================================================

# pets.py


def describe_pet_01(animal_type, pet_name):
    """Positional Arguments//Multiple Funcions Calls//Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Order Matters in Positional Arguments
# describe_pet_01('hamster', 'harry')
# describe_pet_01('dog', 'neptune')
# -----------------------------------------------------------------------


def describe_pet_02(animal_type, pet_name):
    """Keyword Arguments"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Can be switched around and still work
# describe_pet_02(animal_type='hamster', pet_name='harry')
# -----------------------------------------------------------------------

def describe_pet_03(pet_name, animal_type='dog'):
    """Default Values"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Can be switched around and still work
# describe_pet_03(pet_name='neptune')
# describe_pet_03('neptune')
# -----------------------------------------------------------------------

# ============================================================================================================
'''Return Values'''
# ============================================================================================================

# formatted_name.py


def get_formatted_name_01(first_name, last_name):
    """Returning a Simple Value///Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# musician = get_formatted_name_01('jovan', 'dandridge')
# print(musician)
# -----------------------------------------------------------------------

def get_formatted_name_02(first_name, middle_name, last_name):
    """Making an Argument Optional"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


# musician = get_formatted_name_02('jovan', 'terry', 'dandridge')
# print(musician)
# -----------------------------------------------------------------------


def get_formatted_name_03(first_name, last_name, middle_name=''):
    """Making an Argument Optional"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# musician = get_formatted_name_03('jovan', 'terry', 'dandridge')
# print(musician)
# musician = get_formatted_name_03('jacob', 'dandridge')
# print(musician)
# -----------------------------------------------------------------------

# person.py
def build_person_01(first_name, last_name):
    """Returning a Dictionary///Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


# musician = build_person_01('jovan', 'dandridge')
# print(musician)
# -----------------------------------------------------------------------


def build_person_02(first_name, last_name, age=None):
    """Returning a Dictionary///Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person_02('jovan', 'dandridge', age=31)
# print(musician)
# -----------------------------------------------------------------------


def get_formatted_name_04(first_name, last_name):
    """Using a Function with a while loop"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name_04(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")
# ============================================================================================================
'''Passing a List'''
# ============================================================================================================

# greet_users.py


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
# -----------------------------------------------------------------------

"""Modifying a List in a Function"""
# printing_models.py


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing eac design, until none are left
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that wre printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs[:], completed_models)   #[:] Prevents a funciton from modifing a list
# show_completed_models(completed_models)

# ============================================================================================================
'''Passing an Arbitary Number of Arguments'''
# ============================================================================================================

# pizza.py


def make_pizza_01(*toppings):
    """Print the list of topping that have been requested."""
    print(toppings)


# make_pizza_01('pep')
# make_pizza_01('sas', 'black olives', 'jal', 'extra cheese')
# -----------------------------------------------------------------------

def make_pizza_02(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza_02('pep')
# make_pizza_02('sas', 'black olives', 'jal', 'extra cheese')
# -----------------------------------------------------------------------

def make_pizza_03(size, *toppings):
    """Mixing Positional and Arbitrary Arguments"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza_03(12, 'pepporoni')
# make_pizza_03(16, 'extra cheese', 'black olives')
# -----------------------------------------------------------------------

# user_profile.py
def build_profile(first, last, **user_info):
    """
    Using Arbitrary Keyword Arguments///Build a dictionary containg everything we know about the user
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('jovan', 'dandridge',
                             location='colorado',
                             field='python')
print(user_profile)

# ============================================================================================================
'''Storing Your Functions in Modules'''
# ============================================================================================================

"""Importing an Entire Module"""
# pizza.py is the module
# module_name.funciton.name() to use the funcitons in a module
# pizza.make_pizza()

"""Importing Specific Functions"""

# make_pizz(12, 'pepperoni')
# function_2(12, 'pepperoni', 'deep dish')

"""Using 'as' to Give a Function an Alias"""
# mp(15, 'extra cheese')

"""Using 'as' to Give a Module an Alias"""
# p.make_pizza(16, 'black olives')

"""Importing All Functions in a Module"""
# make_pizza(12, 'green crack')
