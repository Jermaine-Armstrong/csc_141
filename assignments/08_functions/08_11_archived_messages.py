def show_messages(messages):
    for message in messages:
        print(message)

def archive_messages(messages, archived_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Archiving message: {current_message}")
        archived_messages.append(current_message)
    
messages = ["Hello, how are you?",
            "Don't forget our meeting tomorrow.",
            "Happy Birthday!",
            "See you soon!",
            "Good luck with your project!"
]

archived_messages = []
archive_messages(messages, archived_messages)
print("\nArchived Messages:")
show_messages(archived_messages)

