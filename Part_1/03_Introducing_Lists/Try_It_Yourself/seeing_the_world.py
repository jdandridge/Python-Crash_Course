'''
Think of at least five places in the world you'd like to visit
-->Store the locations in a list. make sure the list is not in 
alphabetical order.

-->print your list in its original order. dont worry about printing
the list neatly, just print it as a raw Python list

-->use sorted() to print your list in alphabetical order without
modifing teh actual list.

-->show that your list is still in its original order by printing
it again

-->use sorted() to print your list in reverse alphabetical order 
without changing the order of the original list.

-->show that your list is still in its original order by 
printing it again.

-->use reverse() to change the order of your list again. print the
list to show that its order has chaged

-->use reverse() to change the order of your list again. print the 
list to show it's back to its original order.

-->use sort() to change your list so it's stored in alphabetical
order. print the list to show that its order has been chaged.

-->use sort() to change your list so it's stored in reverse 
alphabetical order. print the list to show that its order has 
changed.
'''

placeses = ['colorado springs', 'rialto', 'colton',
            'moreno valley', 'san bernardino', 'medford']

print(placeses)
print(sorted(placeses))
print(placeses)

placeses.reverse()
print(placeses)

placeses.sort()
print('=' * 100)
print(placeses)

placeses.sort(reverse=True)
print('=' * 100)
print(placeses)
