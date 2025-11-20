filename = "learning_python.txt"
with open(filename) as file_object:
    contents = file_object.read()
    print("Original contents:")
    print(contents)

print("\nModified contents:")
with open(filename) as file_object:
    for line in file_object:
        modified_line = line.replace("Python", "Java")
        print(modified_line.strip())