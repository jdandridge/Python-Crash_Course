'''
do the following to create a program that simulates how websites ensure tht 
everyone has a unique username.

--> make a list of five or more usernames called current_users.

--> make another list of five usernames called new_user. make sure one or two 
of the new uersames are also in teh current_ursers list.

--> loop through the new_users list to see if each new username has already 
been used. if it has, print a message that the person will need to enter a 
new username. if a username has not been used, print a message saying that 
the username is avaiable.

--> make sure your comparison is case insensitive. if 'John' has been used, 
'JOHN' should not be accepted. to do this, you'll need to make a copy current_users 
containing the lowercae versions of all existing users.
'''

current_users = ['jojo85', 'admin22', 'mike16', 'koko78', 'kobe24']
uppercase = current_users[:]
new_users = ['jojo85', 'dnuts82', 'kobe24', 'brobro66', 'jake05']

username = input('Choose username\n>>> ')

for new in new_users:
    if new == username and username.title():
        print(f"Welcome back {new.title()}")
        break
    else:
        print('username is availabe')
        break
