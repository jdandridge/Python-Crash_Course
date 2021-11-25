"""Working with Multiple Files"""


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass    # Failing Silently
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick', 'little_women.txt']
for f in filenames:
    count_words(f)
