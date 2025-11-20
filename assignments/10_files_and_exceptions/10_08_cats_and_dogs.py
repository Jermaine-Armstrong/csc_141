filename = ['cats.txt', 'dogs.txt']

for file in filename:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        print(f"Contents of {file}:\n{contents}\n")