def make_sandwich(*items):
    print("Making a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese', 'mustard', 'pickles', 'onions')
make_sandwich('peanut butter', 'jelly')
print("All sandwiches are ready!")

def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album
album1 = make_album('Adele', '25')
album2 = make_album('The Weeknd', 'After Hours', 14)
print(album1)
print(album2)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
messages = ["Hello!", "How are you?", "Don't forget our meeting."]
sent_messages = []
send_messages(messages, sent_messages)
print("\nSent Messages:")
for messages in sent_messages:
    print(messages)