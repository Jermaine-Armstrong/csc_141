favorite_languages = {
    'ashlin': 'python',
    'brandon': 'c',
    'kamerin': 'ruby',
    'kendall': 'python',
    'caleb': 'java',
}

people_to_poll = ['kendall', 'kamerin', 'brandon', 'ashlin', 'caleb']

for person in people_to_poll:
    if person in favorite_languages:
        language = favorite_languages[person]
        print(f"Thank you for taking the poll, {person.title()}! I see your favorite language is {language}.")
    else:
        print(f"{person.title()}, please take our poll!")