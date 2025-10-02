for age in [2, 4, 12, 20, 65]:
    if age < 2:
        stage = 'a baby'
    elif age < 4:
        stage = 'a toddler'
    elif age < 13:
        stage = 'a kid'
    elif age < 20:
        stage = 'a teenager'
    elif age < 65:
        stage = 'an adult'
    else:
        stage = 'an elder'
    print(f"At age {age}, a person is {stage}.")