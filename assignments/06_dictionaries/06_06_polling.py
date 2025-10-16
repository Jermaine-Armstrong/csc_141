favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'louis': 'java',
}

people_to_poll = ['jen', 'edward', 'mike', 'louis', 'anna']

for person in people_to_poll:
    if person in favorite_languages:
        language = favorite_languages[person]
        print(f"Thank you for taking the poll, {person.title()}! I see your favorite language is {language}.")
    else:
        print(f"{person.title()}, please take our poll!")