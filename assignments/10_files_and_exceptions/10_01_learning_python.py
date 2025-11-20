filename = "learning_python.txt"
with open(filename) as file_object:
    contents = file_object.read()
    print("Contents of the file:")
    print(contents)

print("\nReading line by line:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())