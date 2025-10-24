favorite_numbers = {
    'Jermiane': [11, 3],
    'Talia': [7, 1],
    'Owen': [2, 4],
    'Angel': [25, 7],
    'Bam': [2, 6],
    'Zoe': [5, 8],
    'Mia': [7, 10],
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is:")
    for num in number:
        print(f"- {num}")