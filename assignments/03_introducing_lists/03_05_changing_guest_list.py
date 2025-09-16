guests = ["Tania", "Dominick", "Talia"]

for guest in guests:
    print(f"Hi {guest}, you are invited to dinner at my place!")

cantmakeit = "Dominick"
print(f"\nUnfortunately, {cantmakeit} can’t make it to the dinner.\n")

guests[guests.index(cantmakeit)] = "Kareem"

for guest in guests:
    print(f"Hi {guest}, you are still invited to dinner at my place!")
