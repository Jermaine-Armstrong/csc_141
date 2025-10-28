def show_messages(messages):
    for message in messages:
        print(message)

print("Sending Messages:")

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello, how are you?",
            "Don't forget our meeting tomorrow.",
            "Happy Birthday!",
            "See you soon!",
            "Good luck with your project!"
]

sent_messages = []
send_messages(messages, sent_messages)
print("\nSent Messages:")
show_messages(sent_messages)