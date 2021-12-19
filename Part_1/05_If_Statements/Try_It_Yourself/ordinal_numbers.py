'''
ordinal numbers indicate their positin in a list, such as 1st or 2nd. most 
ordinal numbers end in the,except 1, 2, and 3.

--> store teh numbers 1 through 9 in a list.

--> loop through the list.

--> use an if-elif-else chain inside the loop to print the porper ordinal 
ending for each number. yuour output should read '1st 2nd 3rd 4th 5th 6th 7th 8th 9th', 
and each result should be on a separate line.
'''

ordinal_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in ordinal_num:
    if x == 1:
        print(str(x) + 'st')
    elif x == 2:
        print(str(x) + 'nd')
    elif x == 3:
        print(str(x) + 'rd')
    else:
        print(str(x) + 'th')
