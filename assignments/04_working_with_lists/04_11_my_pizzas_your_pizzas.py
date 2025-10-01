pizzas = ["Pepperoni","Sausage","Bacon"]

friend_pizzas = pizzas[:]

pizzas.append("Buffalo")

friend_pizzas.append("Veggie")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
