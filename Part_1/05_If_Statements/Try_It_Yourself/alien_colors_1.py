'''
imagine an alien was just shot down in a game. crate a variable called alien_color 
and assign it a value of 'green', 'yellow', or 'red'.

--> write an if statement to test whether the aliens's color is green. if it is 
print a message that the player just earned 5 points.

--> write one version of this program that passes the if test and another that fails. 
the version that fails will have no output
'''

alien_color = 'red'
if alien_color == 'red':
    print('You just got 5 points')

if alien_color == 'green':
    print('Wrong color')

if alien_color != 'green':
    print('Wrong color')
