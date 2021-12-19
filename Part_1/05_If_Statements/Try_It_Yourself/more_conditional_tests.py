'''
you dont have to limit the number of tests you create to ten. if you want to try more 
comperisons, write more test and add them to conditional_tests.py. have at least one 
true and one false result for each of the following

--> tests for equality and inequality with strings

--> tests using the lower() method

--> numerical tests involving equality and inequality, grater than and less than, 
greater then or equal to, and less than or equal to

--> tests using the and keyword and the or keyword

--> test whether an item is in a list

--> test whether an item is not in a list
'''

car = 'Honda'
print(car == 'Honda')                       # True
print(car.lower() == 'Honda')               # False

answer = 3
print(answer > 6)
print(answer >= 6)
print(answer < 6)
print(answer <= 6)
print(answer != 6)
print(answer != 6 and answer < 6)
print(answer != 3 and answer < 1)
print(answer != 3 or answer > 7)

print('=' * 100)

names = ['jovan', 'jacob', 'dakota', 'nishia']
print('jove' in names)
print('jovan' in names)
