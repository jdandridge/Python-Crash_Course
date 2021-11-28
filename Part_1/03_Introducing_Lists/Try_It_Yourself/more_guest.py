'''
You just found a bigger dinner table, so now more space is 
available. Think of threee more guests to invite to dinner.
--start with your program from exercise 3-4 or 3-5. add a print()
call to the end of your program informing people that you found
a bigger dinnner table
--use insert() to add one new guest to the beginning of your list.
--use insert() to add one new guest to the middle fo your list.
--use append() to add one new guest to the end of your list.
--print a new set of invitation messages, one for each person 
in your list
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
