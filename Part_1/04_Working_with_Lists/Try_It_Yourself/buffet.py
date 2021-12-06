'''
a buffet-style restaurant offers only five basic foods. think of five simple
foods, and store them in a tuple.

--> use a for loop to print each food the restaurant offers

--> try to modify one of the items, and make sure that python rejects the change

--> the restaurant changes its menu, replacing two of the items with different
foods. add a line that rewrites the tuple, and the use a for loop to print each
of the items on the revised menu
'''

buffets = ('pizza', 'burger', 'sushi', 'hot dog', 'cake')

for x in buffets:
    print(x)

buffets = ('dog', 'cat')
for x in buffets:
    print(x)


# buffets[0] = 'dog'
# print(buffets)
