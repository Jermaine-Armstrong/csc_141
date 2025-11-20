def count_the_words(filename, word):
    """Count occurrences of a specific word in a file."""
    try:
        with open(filename, 'r') as file:
            contents = file.read().lower()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        return 0
    else:
        words = contents.split()
        count = words.count(word.lower())
        return count
    