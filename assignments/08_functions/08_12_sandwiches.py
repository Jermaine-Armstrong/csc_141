def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'bacon', 'avocado')
make_sandwich('peanut butter', 'jelly')

print("Your sandwiches are ready!")