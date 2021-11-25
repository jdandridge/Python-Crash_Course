# ============================================================================================================
'''Chapter 4 Working With Lists'''
# ============================================================================================================
"""In Chapter 3 you learned how to make a simple list, and you learned to work with the individual elements in 
a list. In this chapter you'll learn how to loop through an entire list using just a few lines of code 
regardless of how long the list is. Looping allows you to take the same action, or set of actions, with every 
item in a list. As a result, you'll be able to work efficiently with lists of any length, including those with
thousands or even millions of items"""

# ============================================================================================================
'''Loopoing Through an Entire List'''
# ============================================================================================================


def loop_01():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician)


# loop_01()


def loop_02():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")


# loop_02()

def loop_03():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")


# loop_03()

def loop_04():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you, everyone. That was a great magic show!")


# loop_04()

# ============================================================================================================
'''Making Numerical Lists'''
# ============================================================================================================


def range_01():
    for value in range(1, 5):
        print(value)


# range_01()

def range_02():
    numbers = list(range(1, 6))
    print(numbers)


# range_02()

def range_03():
    even_numbers = list(range(2, 11, 2))
    print(even_numbers)


# range_03()

def range_04():
    squares = []
    for value in range(1, 11):
        square = value ** 2  # create instance
        squares.append(square)  # add to the list
    print(squares)  # print list


# range_04()

def range_05():
    squares = []
    for value in range(1, 11):
        squares.append(value ** 2)
    print(squares)


# range_05()

def range_06():
    '''Simple Statistics with a List of Numbers'''
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(min(digits))
    print(max(digits))
    print(sum(digits))


# range_06()

def range_07():
    '''List Comprehensions'''
    squares = [value**2 for value in range(1, 11)]
    print(squares)


# range_07()

# ============================================================================================================
'''Working with Part of a List'''
# ============================================================================================================


def slicing_01():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])


# slicing_01()

def slicing_02():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[1:4])


# slicing_02()

def slicing_03():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[:4])


# slicing_03()

def slicing_04():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[2:])


# slicing_04()

def slicing_05():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[-3:])


# slicing_05()

def slicing_06():
    '''Looping Through a Slice'''
    players = ['charles', 'martina', 'michael', 'florence', 'eli']

    print("Here are the first three players on my team")
    for player in players[:3]:
        print(player.title())


# slicing_06()

def slicing_07():
    '''Copying a List'''
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friends_food = my_foods[:]  # new list made from the first

    print("My favorite foods are:")
    print(my_foods)

    print("\nMy friend's favorite foods are:")
    print(friends_food)


# slicing_07()

def slicing_08():
    '''Copying a List'''
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friends_food = my_foods[:]  # new list made from the first

    my_foods.append('cannoli')
    friends_food.append('ice cream')

    print("My favorite foods are:")
    print(my_foods)

    print("\nMy friend's favorite foods are:")
    print(friends_food)


# slicing_08()

# ============================================================================================================
'''Tuples'''
# ============================================================================================================


def tuples_01():
    '''Defining a Tuple'''
    dimensions = (200, 50)
    print(dimensions[0])
    print(dimensions[1])


# tuples_01()

def tuples_02():
    '''Looping Through All Values in a Tuple'''
    dimensions = (200, 50)
    for dimension in dimensions:
        print(dimension)


# tuples_02()


def tuples_03():
    '''Writing over a Tuple'''
    dimensions = (200, 50)

    print("Original dimensions:")
    for dimension in dimensions:
        print(dimension)

    dimensions = (400, 100)
    print("\nModified dimensions")
    for dimension in dimensions:
        print(dimension)


tuples_03()
