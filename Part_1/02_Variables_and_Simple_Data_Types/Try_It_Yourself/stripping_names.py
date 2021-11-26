'''
Use a variable to represent a person's name, and include some whitespace
characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace arond the name is displayed.
Then print the name using each of the three stripping functions,
lstrip(), rstrip(), and strip().
'''

name = '\tjovan'
name_2 = '\njacob\n'

print(name)
print(name_2)
print('=' * 50)
print(name.strip())
print(name_2.strip())
print('=' * 50)
print(name.lstrip())
print(name_2.lstrip())
print('=' * 50)
print(name.rstrip())
print(name_2.rstrip())
