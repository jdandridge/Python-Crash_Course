# ============================================================================================================
'''Chapter 6 Dictionaries'''
# ============================================================================================================
"""In this chapter you'll learn how to use Pythons's dictionaries, which allow you to connect pieces of 
related information. You'll learn how to access the information once it's in a dictionary and how to modify 
that information. Because dictionaries can store an almost limitless amount of information, I'll show you how
to loop through the data in a dictionary."""

# ============================================================================================================
'''A Simple Dictionary'''
# ============================================================================================================


def alien_00():
    alien_0 = {
        'color': 'green',
        'points': 5
    }

    print(alien_0['color'])
    print(alien_0['points'])


# alien_00()

# ============================================================================================================
'''Working with Dictionaries'''
# ============================================================================================================


def alien_01():
    '''Accessing Values in a Dictionary'''
    alien_0 = {
        'color': 'green',
        'points': 5
    }

    new_points = alien_0['points']
    print(f"You just earned {new_points} points!")


# alien_01()


def alien_02():
    '''Adding New Key-Value Pairs'''
    alien_0 = {
        'color': 'green',
        'points': 5
    }
    print(alien_0)

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25

    print(alien_0)


# alien_02()

def alien_03():
    '''Starting with an Empty Dictionary'''
    alien_0 = {}

    alien_0['color'] = 'green'
    alien_0['points'] = 5

    print(alien_0)


# alien_03()


def alien_04():
    '''Modifying Values in a Dictionary'''
    alien_0 = {'color': 'green'}
    print(f"The alien is {alien_0['color']}")

    alien_0['color'] = 'yellow'
    print(f"The alien is now {alien_0['color']}")


# alien_04()

def alien_05():
    '''Modifying Values in a Dictionary'''
    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print(f"Original position: {alien_0['x_position']}")

    # Move the alien to the right
    # Determine how far to move the alien based on its current speed
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        # This must be a fast alien
        x_increment = 3

    # The new position is the old position plus the increment
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print(f"New position: {alien_0['x_position']}")


# alien_05()


def alien_06():
    '''Removing Key-Value Pairs'''
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)

    del alien_0['points']
    print(alien_0)


# alien_06()


def alien_07():
    '''A Dictionary of Similar Objects'''
    favorite_languages = {
        'jovan': 'python',
        'jacob': 'c',
        'nishia': 'ruby',
        'young': 'python',
    }

    language = favorite_languages['jovan'].title()
    print(f"Jovan's favorite lanuage is {language}.")


# alien_07()

def alien_08():
    '''Using get() to Access Values'''
    alien_0 = {'color': 'green', 'speed': 'slow'}
    point_value = alien_0.get('points', 'No point value assigned.')

    print(point_value)


# alien_08()

# ============================================================================================================
'''Looping Through a Dictionary'''
# ============================================================================================================


def user_01():
    '''Looping Through All Key-Value Pairs'''
    user_0 = {
        'username': 'jovan03',
        'first': 'jovan',
        'last': 'dandridge',
    }

    for key, value in user_0.items():
        print(f"\nKey: {key}")
        print(f"Value: {value}")


# user_01()


def user_02():
    '''Looping Through All Key-Value Pairs'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    for name, language in favorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}.")


# user_02()

def user_03():
    '''Looping Through All the Keys in a Dictionary'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    for name in favorite_languages.keys():
        print(name.title())


# user_03()

def user_04():
    '''Looping Through All the Keys in a Dictionary'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    friends = ['phil', 'sarah']
    for name in favorite_languages.keys():
        print(f"Hi {name.title()}.")

        if name in friends:
            language = favorite_languages[name].title()
            print(f"\t{name.title()}, I see you love {language}!")


# user_04()

def user_05():
    '''Looping Through All the Keys in a Dictionary'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")


# user_05()


def user_06():
    '''Looping Through a Dictionary's Keys in a Particular Order'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, thank you for taking the poll.")


# user_06()

def user_07():
    '''Looping Through All Values in a Dictionary'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    print("The following languages have been mentioned:")
    for language in favorite_languages.values():
        print(language.title())


# user_07()

def user_08():
    '''Looping Through All Values in a Dictionary'''
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    print("The following languages have been mentioned:")
    # use set() when you have duplicate itemes
    for language in set(favorite_languages.values()):
        print(language.title())


# user_08()

# ============================================================================================================
'''Nesting'''
# ============================================================================================================


def nest_01():
    '''A List of Dictionaries'''
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}

    aliens = [alien_0, alien_1, alien_2]

    for alien in aliens:
        print(alien)


# nest_01()


def nest_02():
    '''A List of Dictionaries'''
    # Make an empty list for storing aliens
    aliens = []

    # Make 30 green aliens.
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    # Show the first 5 aliens.
    for alien in aliens[:5]:
        print(alien)
    print("...")

    # Show how many aliens have been created.
    print(f"Total number of aliens: {len(aliens)}")


# nest_02()

def nest_03():
    '''A List of Dictionaries'''
    # Make an empty list for storing aliens
    aliens = []

    # Make 30 green aliens.
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10

    # Show the first 5 aliens.
    for alien in aliens[:5]:
        print(alien)
    print("...")

    # Show how many aliens have been created.
    print(f"Total number of aliens: {len(aliens)}")


# nest_03()

def nest_04():
    '''A List of Dictionaries'''
    # Make an empty list for storing aliens
    aliens = []

    # Make 30 green aliens.
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

    # Show the first 5 aliens.
    for alien in aliens[:5]:
        print(alien)
    print("...")

    # Show how many aliens have been created.
    print(f"Total number of aliens: {len(aliens)}")


# nest_04()

def nest_05():
    '''A List in a Dictionary'''
    # Store information about a pizza being ordered.
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
    }

    # Summarize the order
    print(f"You ordered a {pizza['crust']}-crust pizza "
          "with the following toppings:")

    for topping in pizza['toppings']:
        print(f"\t{topping}")


# nest_05()

def nest_06():
    '''A List in a Dictionary'''
    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
    }

    for name, languages in favorite_languages.items():
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")


# nest_06()

def nest_07():
    '''A Dictionary in a Dictionary'''
    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
    }

    for username, user_info in users.items():
        print(f"\nUsername: {username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']

        print(f"\tFull name: {full_name.title()}")
        print(f"\tLocation: {location.title()}")


nest_07()
