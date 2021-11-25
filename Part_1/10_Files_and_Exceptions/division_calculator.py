# ============================================================================================================
'''Chapter 10 EXCEPTIONS// Pg.194'''
# ============================================================================================================


def handle_00():
    '''Handling the ZeroDivisionError Exception'''
    print(5/0)


# handle_00()


def handle_01():
    '''Using try-except Blocks'''
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")


# handle_01()

def handle_02():
    '''Using Exceptions to Prevent Crashes'''
    print("Give me two numbers, and I'll divide them")
    print("Enter 'q' to quit")

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        answer = int(first_number) / int(second_number)
        print(answer)


# handle_02()

def handle_03():
    '''The else Block'''
    print("Give me two numbers, and I'll divide them")
    print("Enter 'q' to quit")

    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)


# handle_03()


def handle_04():
    '''Handling the FileNotFoundError Exception'''
    filename = 'alice.txt'

    with open(filename, encoding='utf-8') as f:
        contents = f.read()


# handle_04()

def handle_05():
    '''Handling the FileNotFoundError Exception'''
    filename = 'alice.txt'

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")


# handle_05()

def handle_06():
    '''Analyzing Text'''
    filename = 'alice.txt'

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in a file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


handle_06()
