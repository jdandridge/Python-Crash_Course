def pi_00():
    '''Working with a File's Contents'''
    filename = 'pi_digits.txt'

    with open(filename) as file_objects:
        lines = file_objects.readlines()

    pi_string = ''
    for line in lines:
        # pi_string += line.rstrip()
        pi_string += line.strip()
    print(pi_string)
    print(len(pi_string))


# pi_00()


def pi_01():
    '''Large Files: One Million Digits'''
    filename = 'pi_million_digits.txt'

    with open(filename) as file_objects:
        lines = file_objects.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    print(f"{pi_string[:52]}...")
    print(len(pi_string))


# pi_01()

def pi_02():
    '''Is Your Birthday Contained in Pi?'''
    filename = 'pi_digits.txt'

    with open(filename) as file_objects:
        lines = file_objects.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()

    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birth is there")
    else:
        print("Nope try again")


pi_02()
