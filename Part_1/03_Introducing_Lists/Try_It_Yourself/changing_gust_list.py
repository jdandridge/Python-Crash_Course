'''
You just heard that one of your guest can't make the dinner,
so you need to send out a new set of invitations. You'll 
have to think of someone else to invite.
--start with your program from Exercise 3-4. add a print()
call at the end fo your program stating the name fo the guest
who cant make it.
--Modify your list, replacing the name fo the guest who can't make
it with the name fo the new person you are inviting.
--Print a second set of invitation messages, one for each person who
is still in your list
'''

guest_list = ['Malcom X', 'Don Sharpe', 'Joel']
message = f"{guest_list[2]} wont be able to make it today"
print(message)
guest_list[2] = 'Kevin Sam'
message2 = f"{guest_list[0]}, {guest_list[1]}, {guest_list[2]} are all welcome to the dinner party"
print(message2)
