# ============================================================================================================
'''Chapter 10 WRITING TO A FILE// Pg.191'''
# ============================================================================================================


def writing_00():
    '''Writing to an Empty File'''
    filename = 'programming.txt'

    with open(filename, 'w') as file_objects:
        file_objects.write("I love programming")


# writing_00()


def writing_01():
    '''Writing Multiple Lines'''
    filename = 'programming.txt'

    with open(filename, 'w') as file_objects:
        file_objects.write("I love programming.\n")
        file_objects.write("I love creating new games.\n")


# writing_01()

def writing_02():
    '''Appending to a File'''
    filename = 'programming.txt'

    with open(filename, 'a') as file_objects:
        file_objects.write("I also love finding meaning in large datasets.\n")
        file_objects.write("I love creating apps that can run in a browser.\n")


writing_02()
