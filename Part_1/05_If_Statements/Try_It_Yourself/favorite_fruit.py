'''
make a lilst of your favorite fruits, and then write a series of independent if statements 
that check for certain fruits in your list.

--> make a list of your three favorite fruits and call it favorite_fruits.

--> write five if statements. each shoud check whether a certain kid of fruit is in 
you list. if teh fruit is in you list, the if block should print a statement, such as 
you really like bananas!
'''

favorite_fruits = ['bananas', 'apple', 'watermelon']

if 'apple' in favorite_fruits:
    print("I love me some apples")
if 'bananas' in favorite_fruits:
    print("I love me some bananas")
if 'watermelon' in favorite_fruits:
    print("I love me some watermelon")
if 'apple' in favorite_fruits:
    print("I love me some apples")
if 'apple' or 'bananas' in favorite_fruits:
    print("I love me some apples and bananas")
