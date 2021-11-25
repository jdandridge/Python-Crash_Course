# ============================================================================================================
'''Chapter 3 Introducing Lists'''
# ============================================================================================================
"""In this chapter and the next you'll learn what lists are and how to start working with the elements in a 
list. Lists allow you to store sets of information in one place, whether you have just a few items or millions
of items. List are one of Python's most powerful features readily accessible to new programmers, and they tie
together many important concepts in programming."""

# ============================================================================================================
'''Lists'''
# ============================================================================================================


def list_01():
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles)


# list_01()


def list_02():
    '''Accessing Elements in a List'''
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles[0])
    print(bicycles[0].title())


# list_02()

def list_03():
    '''Accessing Elements in a List'''
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    message = f"My first bicycle was a {bicycles[0].title()}."
    print(message)


# list_03()

def list_04():
    '''Modifying Elements in a List'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles[0] = 'ducati'
    print(motorcycles)


# list_04()

def list_05():
    '''Adding Elements to a list:Appending Elements to the End of a list'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.append('ducati')
    print(motorcycles)


# list_05()


def list_06():
    '''Adding Elements to a list:Inserting Elements into a List'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.insert(0, 'ducati')
    print(motorcycles)


# list_06()

def list_07():
    '''Removing Elements from a List:Removing an Item using the 'del' statement'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    del motorcycles[0]
    print(motorcycles)


# list_07()


def list_08():
    '''Removing Elements from a List:Removing an Item using the 'pop()' Method'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    popped_motorcycle = motorcycles.pop()
    print(motorcycles)
    print(popped_motorcycle)


# list_08()


def list_09():
    '''Removing Elements from a List:Removing an Item using the 'pop()' Method'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    last_owned = motorcycles.pop()
    print(f"The last motorcycle I owned was a {last_owned.title()}.")


# list_09()


def list_10():
    '''Removing Elements from a List:Removing an Item using the 'pop()' Method'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    first_owned = motorcycles.pop(0)
    print(f"The first motorcyle i owned was a {first_owned.title()}.")


# list_10()


def list_11():
    '''Removing Elements from a List:Removing an item by value'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.remove('honda')
    print(motorcycles)


# list_11()


def list_12():
    '''Removing Elements from a List:Removing an item by value'''
    motorcycles = ['honda', 'yamaha', 'suzuki']
    too_expensive = 'yamaha'
    motorcycles.remove(too_expensive)
    print(motorcycles)
    print(f"\nA {too_expensive.title()} is too expensive for me.")


# list_12()

# ============================================================================================================
'''Organizing a Lists'''
# ============================================================================================================


def org_list_01():
    '''Sorting a List Permanently with the 'sort() Method'''
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()
    print(cars)


# org_list_01()

def org_list_02():
    '''Sorting a List Temporarily with the sorted() function'''
    cars = ['bmw', 'audi', 'toyota', 'subaru']

    print('Here is the original list:')
    print(cars)

    print('\nHere is the sorted list:')
    print(sorted(cars))

    print('\nHere is the original list:')
    print(cars)


# org_list_02()


def org_list_03():
    '''Printing a List in Reverse Order'''
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(cars)

    cars.reverse()
    print(cars)


# org_list_03()


def org_list_04():
    '''Finding the Length of a List'''
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print(len(cars))


org_list_04()
