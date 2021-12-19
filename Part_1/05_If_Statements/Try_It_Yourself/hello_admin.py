'''
make a list of five or more usernames, including the name 'admin'. imagine you 
are writing code that will print a greeting to each user after they log in to a 
website. loop through the list, and print a greeting to each user:

--> if the username is 'admin', print a special greeting, such as hello admin, 
would you like to see a status report

--> otherwise, print a generic greeting, such as hello jaden, thank you for 
logging in again
'''

usernames = ['jojo05', 'admin45', 'mike16', 'john78', 'use36']

for username in usernames:
    if username == 'admin45':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Login {username}")
