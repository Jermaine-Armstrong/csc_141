def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'Jermaine', 'Armstrong',
    location='Baltimore',
    field='Computer Science',
    sport='Football',
    position='Defensive Back'
)

print(my_profile)
