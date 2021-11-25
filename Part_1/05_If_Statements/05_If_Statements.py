# ============================================================================================================
'''Chapter 5 If Statements'''
# ============================================================================================================
"""Programming often involves examining a set of conditions and deciding which action to take based on those 
conditions. Python's if statements allows you to examine the current state of a program and respond 
appropriately to that state."""

# ============================================================================================================
'''A Simple Example'''
# ============================================================================================================


def example_01():
    cars = ['audi', 'bmw', 'subaru', 'toyota']

    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())


# example_01()

# ============================================================================================================
'''Conditional Tests'''
# ============================================================================================================


def check_01():
    '''Checking for Equality: True'''
    car = 'bmw'
    print(car == 'bmw')


# check_01()

def check_02():
    '''Checking for Equality: False'''
    car = 'audi'
    print(car == 'bmw')


# check_02()

def check_03():
    '''Ignoring Case When Checking for Equality: False'''
    car = 'Audi'
    print(car == 'audi')


# check_03()

def check_04():
    '''Ignoring Case When Checking for Equality: True'''
    car = 'Audi'
    print(car.lower() == 'audi')
    print(car)


# check_04()

def check_05():
    '''Checking for Inequality'''
    requested_topping = 'mushrooms'

    if requested_topping != 'anchovies':
        print('Hold the anchovies!')


# check_05()

def check_06():
    '''Numerical Comparisons'''
    age = 18
    true_value = age == 18
    print(true_value)


# check_06()


def check_07():
    '''Numerical Comparisons'''
    answer = 17
    if answer != 42:
        print('That is not the correct answer. Please tryi again!')


# check_07()

def check_08():
    '''Numerical Comparisons'''
    age = 19

    print(age < 21)
    print(age <= 21)
    print(age > 21)
    print(age >= 21)


# check_08()

def check_09():
    '''checking Multiple Conditions: Using 'and' to check multiple conditions'''
    age_0 = 22
    age_1 = 18
    false_expression = age_0 >= 21 and age_1 >= 21  # both have to be True

    print(false_expression)


# check_09()

def check_10():
    '''checking Multiple Conditions: Using 'and' to check multiple conditions'''
    age_0 = 22
    age_1 = 22
    true_expression = age_0 >= 21 and age_1 >= 21  # both have to be True

    print(true_expression)


# check_10()

def check_11():
    '''checking Multiple Conditions: using 'or' to check multiple conditions'''
    age_0 = 22
    age_1 = 18
    # both have to be False to pass False
    true_expression = age_0 >= 21 or age_1 >= 21

    print(true_expression)


# check_11()

def check_12():
    '''checking Multiple Conditions: using 'or' to check multiple conditions'''
    age_0 = 18
    age_1 = 18
    # both have to be False to pass False
    false_expression = age_0 >= 21 or age_1 >= 21

    print(false_expression)


# check_12()

def check_13():
    '''Checking Whether a Value is in a List'''
    requested_toppings = ['mushrooms', 'onions', 'pineapple']
    print('mushrooms' in requested_toppings)  # True
    print('peperoni' in requested_toppings)  # False


# check_13()

def check_14():
    '''Checking Whether a Value is Not in a List'''
    banned_users = ['andrew', 'carolina', 'david']
    user = 'jovan'

    if user not in banned_users:
        print(f"{user.title()}, you can post a response if you wish.")


# check_14()

def check_15():
    '''Boolean Expressions'''
    game_active = True
    can_edit = False


# check_15()

# ============================================================================================================
'''if Statements'''
# ============================================================================================================


def statements_01():
    age = 19
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")


# statements_01()


def statements_02():
    '''if-else Statements'''
    age = 17
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
        print("Sorry, you are to young to vote.")
        print("Please register to vote as soon as you turn 18!")


# statements_02()

def statements_03():
    '''The if-elif-else Chain'''
    # Admission for anyone under age 4 is free
    # Admission for anyone between the ages of 4 and 18 is $25
    # Admission for anyone age 18 or older is $40

    age = 12
    if age < 4:
        print("Your admission cost is $0")
    elif age < 18:
        print("Your admission cost is $25")
    else:
        print("Your admission cost is $40")


# statements_03()

def statements_04():
    '''The if-elif-else Chain'''
    age = 12

    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    else:
        price = 40

    print(f"Your admission cost is ${price}.")


# statements_04()

def statements_05():
    '''Using Multiple elif Blocks'''
    age = 12

    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    elif age < 65:
        price = 40
    else:
        price = 20

    print(f"Your admission cost is ${price}.")


# statements_05()

def statements_06():
    '''Omitting the else Block'''
    age = 12

    if age < 4:
        price = 0
    elif age < 18:
        price = 25
    elif age < 65:
        price = 40
    elif age >= 65:
        price = 20

    print(f"Your admission cost is ${price}.")


# statements_06()

def statements_07():
    '''Testing Multiple Conditions'''
    requested_toppings = ['mushrooms', 'extra cheese']

    if 'mushrooms' in requested_toppings:
        print("Adding mushrooms")
    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni")
    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese")

    print("\nFinished making your pizza!")


# statements_07()

# ============================================================================================================
'''Using if Statements with Lists'''
# ============================================================================================================


def toppings_01():
    '''Checking for special items'''
    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")


# toppings_01()


def toppings_02():
    '''Checking for special items'''
    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")


# toppings_02()


def toppings_03():
    '''Checking that a List Not Empty'''
    requested_toppings = []

    if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")


# toppings_03()

def toppings_04():
    '''Using multiple Lists'''
    available_toppings = ['mushrooms', 'olives',
                          'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requesed_toppings = ['mushrooms', 'french fries', 'extra cheese']

    for requesed_topping in requesed_toppings:
        if requesed_topping in available_toppings:
            print(f"Adding {requesed_topping}.")
        else:
            print(f"Sorry, we don't have {requesed_topping}.")

    print("\nFinished making your pizza!")


toppings_04()
