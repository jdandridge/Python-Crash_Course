'''
using one of the programs you wrote in this chapter, add several lines to the end
of the program that do the following:

--> print the messge The first three items in the list are:. then use a slice to
print the first three items from that programs list.

--> print the message three items from the middle fo the list are:. use a slice
to print three items from the middle fo the list.

--> print the message the last three items of the list are:. use a slice to 
print the last three items in the list
'''
toppings = ['pepperoni', 'black olives', 'bacon',
            'extra cheese', 'mushrooms', 'sasuage', 'jalapenos']

print(f"The first three items in the list are: {toppings[0:3]}")
print(f"Three items in the middle list are: {toppings[3:6]}")
print(f"The last three items in the list are: {toppings[4:]}")
