respones = []
while True:
    vacation = input("If you could visit somewhere in the world, where would you go? (Type 'quit' to stop) ")
    if vacation == 'quit':
        break
    respones.append(vacation)
print("\n--- Dream Vacation Destinations ---")
for place in respones:
    print(place)