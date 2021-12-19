'''
add an if test to hello_admin.py to make sure the list of users is not empty

--> if the list is empty, print the message we need to find some users!

--> remove all of the usernames from your list, and make sure the correct 
message is printed
'''

usernames = []

if usernames:
    print(f"{usernames}")
else:
    print('We need to find some users!')
