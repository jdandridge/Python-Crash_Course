'''
you just found out that your new dinner table won't arrive in 
time for the finner, and you have space for only two guests.
--start with program from exercise 3-6. add a new line that prints
a message saying that you can invite only two people for dinner
--use pop() to remove guests from your list one at a time until
only two names remain in your list. Each time you pop a name
from you list, print a message that person letting them know
you're sorry you can't invite them to dinner.
--print a message to each of the two people still on your list,
letting them know they're still invited.
--use del to remove the last two names from your list, so 
you have an empty list. Print your list to make sure you 
actually have an empty list at the end of your program.
'''


guest_list = ['Malcom X', 'Don Sharpe', 'Joel']
print('We found new people to set with us')
guest_list.insert(0, 'Bruce Lee')
guest_list.insert(2, 'Michael Jackson')
guest_list.append('Young Dolph')
print(guest_list)
print(f"Thank you for coming {guest_list[0]}")
print(f"Thank you for coming {guest_list[1]}")
print(f"Thank you for coming {guest_list[2]}")
print(f"Thank you for coming {guest_list[3]}")
print(f"Thank you for coming {guest_list[4]}")
print(f"Thank you for coming {guest_list[5]}")

print('I am very sorry but change of plan can only invite 2 of you')

print(guest_list.pop())
print(guest_list.pop())
print(guest_list.pop())
print(guest_list.pop())
print(guest_list)

print(f"{guest_list[0]} and {guest_list[1]} you are still invited")

del guest_list[0]
del guest_list[0]
print(guest_list)
