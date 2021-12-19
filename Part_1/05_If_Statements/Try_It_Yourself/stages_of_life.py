'''
write an if-elif-else chain that determines a person's stat4e of life. set a value 
for the varable age, and the:

--> if the person is less than 2 years old, print a messge that the person is a baby.

--> if the perosn is at least 2 years old but less then 4, print a messge that the 
person is a toddler.

--> if the person is at least 4 years old but less than 13, print a message that 
the person is a kid.

--> if the person is at leat 13 years old but less than 20, print a messge that 
the peron is a teenager.

--> if the person is at least 20 years old but less than 65, print a message 
that the peron is an adult.

--> if the person is age 65 or older, print a message that the perons is an elder.
'''

print("=" * 100)
print("How old are you?\n")
age = int(input(">>> "))

if age < 2:
    print("You are a baby")
elif age > 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are a adult")
elif age > 65:
    print("You are a elder")
else:
    print("You dont exist")
