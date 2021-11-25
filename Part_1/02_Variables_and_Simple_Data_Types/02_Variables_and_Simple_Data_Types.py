# ============================================================================================================
'''Chapter 2 Variables and Simple Datat Types'''
# ============================================================================================================
"""In this chapter you'll learn about the different kinds of data you can work with in your Python programs.
You'll also learn how to use variables to represent data in your programs"""


# ============================================================================================================
'''Variables'''
# ============================================================================================================


def variables_01():
    message = "Hello Python World!"
    print(message)

# variables_01()


def variables_02():
    message = "Hello Python World!"
    print(message)

    message = "Hello Python Crash Course world!"
    print(message)


# variables_02()

# ============================================================================================================
'''Strings'''
# ============================================================================================================


def strings_01():
    '''Changing Case in a String with Methods'''
    name = "jovan agemo"
    print(name.title())


# strings_01()


def strings_02():
    '''Changing Case in a String with Methods'''
    name = "jovan agemo"
    print(name.upper())
    print(name.lower())


# strings_02()


def strings_03():
    '''Using Variables in Stings'''
    first_name = "jovan"
    last_name = "agemo"
    full_name = f"{first_name} {last_name}"
    print(full_name)


# strings_03()


def strings_04():
    '''Using Variables in Stings'''
    first_name = "jovan"
    last_name = "agemo"
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name.title()}!")


# strings_04()


def strings_05():
    '''Using Variables in Stings'''
    first_name = "jovan"
    last_name = "agemo"
    full_name = f"{first_name} {last_name}"
    message = f"Hello, {full_name.title()}!"
    print(message)


# strings_05()


def strings_06():
    '''Adding Whitespace to Strings with Tabs and Newlines'''
    tabs = "\tPython"
    print(tabs)


# strings_06()


def strings_07():
    '''Adding Whitespace to Strings with Tabs and Newlines'''
    newline = "Languages:\nPython\nC\nJavaScript"
    print(newline)


# strings_07()

def strings_08():
    '''Stripping Whitespace'''
    favorite_language = "Python "
    print(favorite_language.rstrip())


# strings_08()


def strings_09():
    '''Stripping Whitespace Permanently'''
    favorite_language = "Python "
    favorite_language = favorite_language.rstrip()
    print(favorite_language)


# strings_09()


def strings_10():
    '''Stripping Whitespace'''
    favorite_language = " Python "
    print(favorite_language.rstrip())
    print(favorite_language.lstrip())
    print(favorite_language.strip())


# strings_10()

# ============================================================================================================
'''Numbers'''
# ============================================================================================================


def numbers_01():
    '''Integers'''
    add = 5 + 2
    subtract = 3 - 2
    multiply = 2 * 6
    divide = 3 / 2
    exponents = 3 ** 2
    ex_1 = 2 + 3 * 4
    ex_2 = (2 + 3) * 4
    print(add)
    print(subtract)
    print(multiply)
    print(divide)
    print(exponents)
    print(ex_1)
    print(ex_2)


# numbers_01()


def numbers_02():
    '''Floats'''
    add_float = 0.1 + 0.1
    multiply_float = 2 * 0.2
    print(add_float)
    print(multiply_float)


# numbers_02()


def numbers_03():
    '''Integers and Floats'''
    div_float = 4 / 2
    multiply_float = 2 * 3.0
    print(div_float)
    print(multiply_float)


# numbers_03()


def numbers_04():
    '''Underscores in Numbers'''
    universe_age = 14_000_000_000
    print(universe_age)


# numbers_04()


def numbers_05():
    '''Multiple Assignment'''
    x, y, z = 0, 1, 2
    print(x)
    print(y)
    print(z)


# numbers_05()


def numbers_06():
    '''Constants: is a variable that stays the same throught the life of a program. Use capital letters to 
    indicate a variable should be treated as a constant and never be changed'''
    MAX_CONNECTIONS = 5000
    print(MAX_CONNECTIONS)


numbers_06()
