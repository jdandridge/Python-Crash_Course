'''
turn your if-else chain from exercise 5-4 into an if elif-else chan.

--> if the alien is green, print a message that the player earned 5 pints

--> if the alien is yellow, print a message that the player earned 10 points.

--> if teh alien is red, print a message that the player earened  15 pints

--> write three versions of this program, making sure each messge is 
printed for the appropriate color alien.
'''

print('=' * 100)
print('Pick a color and earn some points\n')
print(' red\n yellow\n green')
alien = input('>>>')
if alien == 'green':
    print('5pts')
elif alien == 'yellow':
    print('10pts')
elif alien == 'red':
    print('15pts')
else:
    print("that is not a color or follow the rules")
