# ============================================================================================================
'''Chapter 7 User Input and While Loops// Pg.113'''
# ============================================================================================================
"""Most programs are written to solve an end user's problem. To do so, you usually need to get some 
information from the user. For a simple example, let's say someone wants to find out whether they're old 
enough to vote."""

# ============================================================================================================
'''How the input() Function Works'''
# ============================================================================================================


def parrot_01():
    message = input("Tell me something, and i will repeat it back to you: ")
    print(message)


# parrot_01()

def greeter_01():
    '''Writitng clear Prompts'''
    name = input("Please enter your name: ")
    print(f"\nHello, {name}!")


# greeter_01()


def greeter_02():
    '''Writitng clear Prompts'''
    prompt = "If you tell us who you are, we can personlize the messages you see"
    prompt += "\nWhat is your first name? "

    name = input(prompt)
    print(f"\nHello, {name}!")


# greeter_02()

def age_01():
    '''Using int() to Accept Numerical Input'''
    age = input('How old are you? ')
    age = int(age)
    print(age >= 18)


# age_01()


def age_02():
    '''Using int() to Accept Numerical Input'''
    height = input("How tall are you, in inches? ")
    height = int(height)

    if height >= 48:
        print("\nYou're tall enough to ride!")
    else:
        print("\nYou'll be able to ride when you're a little older.")


# age_02()


def age_03():
    '''Using int() to Accept Numerical Input'''
    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)

    if number % 2 == 0:
        print(f"\nThe number {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")


# age_03()

# ============================================================================================================
'''Introducing while Loops//Pg.118'''
# ============================================================================================================


def counting_01():
    '''The while loop in action'''
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1


# counting_01()


def parrot_01():
    '''Letting the User Choose When to Quit'''
    prompt = "\nTell me something, and i will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    message = ""
    while message != 'quit':
        message = input(prompt)

        if message != 'quit':
            print(message)


# parrot_01()


def parrot_02():
    '''Using a Flag'''
    prompt = "\nTell me something, and i will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "

    active = True
    while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)


# parrot_02()


def cities_01():
    '''Using break to Exit a Loop'''
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.)"

    while True:
        city = input(prompt)

        if city == 'quit':
            break
        else:
            print(f"I'd love to go to city {city.title()}!")


# cities_01()

def counting_02():
    '''Using continue in a Loop'''
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue

        print(current_number)


# counting_02()

def counting_03():
    '''Avoiding Infinite Loops//CRTL-C'''
    x = 1
    while x <= 5:
        print(x)
        # x += 1


# counting_03()

# ============================================================================================================
'''Using a while Loop with Lists and Dictionaries//Pg.124'''
# ============================================================================================================


def conf_01():
    '''Moving Items from One List to Another'''
    # Start with users that need to be verified,
    # and an empty list to hold confirmed users.
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []

    # Verify each user until there are no more uncofirmed users.
    # Move each verified user into the list of confirmed users.
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()

        print(f"Verifing user: {current_user.title()}")
        confirmed_users.append(current_user)

    # Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


# conf_01()


def pets_01():
    '''Removing All Instances of Specific Values from a List'''
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)

    while 'cat' in pets:
        pets.remove('cat')
    print(pets)


# pets_01()

def mount_01():
    '''Filling a Dictionary with User Input'''
    responses = {}

    # Set a flag to indicate that polling is active.
    polling_active = True

    while polling_active:
        # Prompt for the person's name and response
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")

        # Store the response in the dictionary.
        responses[name] = response

        # Find out if anyone else is going to take a poll.
        repeat = input(
            "Would you like to let another person respond? (yes/ no) ")
        if repeat == 'no':
            polling_active = False

        # Polling is complete. Show the results
        print("\n--- Poll Results ---")
        for name, response in responses.items():
            print(f"{name.title()} would like to climb {response.title()}.")


# mount_01()


def mount_02():
    '''Filling a Dictionary with User Input'''
    responses = {}

    # Set a flag to indicate that polling is active.
    polling_active = True

    while polling_active:
        # Prompt for the person's name and response
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")

        # Store the response in the dictionary.
        responses[name] = response

        # Find out if anyone else is going to take a poll.
        repeat = input(
            "Would you like to let another person respond? (yes/ no) ")
        if repeat == 'no':
            polling_active = False

        # Polling is complete. Show the results
        print(responses.keys())


mount_02()
