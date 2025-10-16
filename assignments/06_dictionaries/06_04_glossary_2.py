glossary = {
    'variable': 'A named location used to store data in the memory.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure that repeats a block of code as long as a specified condition is true.',
    'list': 'An ordered collection of items that can be of different types.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a value.',
    'boolean': 'A data type that can hold one of two values: True or False.',
    'string': 'A sequence of characters enclosed in quotes.',
    'integer': 'A whole number, positive or negative, without decimals.',
    'comment': 'A note in the code that is ignored by the interpreter, used to explain the code.',
    'if statement': 'A control structure that executes a block of code if a specified condition is true.',
}

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}\n")