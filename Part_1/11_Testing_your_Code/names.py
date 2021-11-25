from name_function import get_formatted_name as gfn

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Pleas give me a last name: ")
    if last == 'q':
        break

    formatted_name = gfn(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
