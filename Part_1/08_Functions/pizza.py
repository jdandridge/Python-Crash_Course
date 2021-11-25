def make_pizza(size, *toppings):
    """Mixing Positional and Arbitrary Arguments"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
