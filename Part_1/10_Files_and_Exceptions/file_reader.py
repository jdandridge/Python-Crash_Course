def reader_00():
    '''Reading an Entire File'''
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()

    print(contents)

    # print(contents.rstrip())
# reader_00()


def reader_01():
    '''Reading Line by Line'''
    filename = 'pi_digits.txt'

    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())


# reader_01()

def reader_02():
    '''Making a List of Lines from a File'''
    filename = 'pi_digits.txt'

    with open(filename) as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


reader_02()
