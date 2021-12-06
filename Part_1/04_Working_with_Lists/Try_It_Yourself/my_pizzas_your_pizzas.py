'''
start with your program from exercise 4-1. make a copy fo the list of pizzas, and
call it friend_pizzas. then, do the following

--> add a new pizza to the original list.

--> add a different pizza to the list friend_pizzas.

--> prove that you have two separate lists. print the message my favorite pizzas are:
and then use a for loop to print the second list. make sure each new pizza is 
stored in the appropriate list
'''


pizzas = ['pepperoni', 'cheese', 'chicken']
friend_pizzas = pizzas[:]

print("my fav food are:")
pizzas.append('beef')
print(pizzas)


print("\nmy friend fav food are:")
friend_pizzas.append('vegan')
print(friend_pizzas)

print("My fav pizzas are:")
for x in pizzas:
    print(x)
print("\nMy friend fav pizzas are:")
for y in friend_pizzas:
    print(y)
