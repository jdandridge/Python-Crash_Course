'''
all versions of foods.py in this section have avoided using for loops when printing
to save space. choose a version of foods.py, and write two for loops to print
each list of foods
'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]  # new list made from the first

my_foods.append('cannoli')
friends_food.append('ice cream')

print("my fav food are:")
for x in my_foods:
    print(x)

print('\nFriend fav food are:')
for y in friends_food:
    print(y)
