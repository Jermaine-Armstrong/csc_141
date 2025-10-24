sandwich_orders = ['ham', 'veggie', 'pastrami', 'turkey']
finished_sandwiches = []
print("The Deli is out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches are made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")