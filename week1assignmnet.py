#variant12
pet_name = input('What is your pet\'s name? ')
pet_type = input('What is your pet\s type?')
pet_age = input('How old your pet?')
fav_toy = input('What is your favourite toy?')
shelter_name = input('What is your shelter name?')


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('          -- ADOPT ME! --               ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print(f'Hi, my name is {pet_name}!\n')
print(f'I am a {pet_age} {pet_type}.')
print(f'My favorite toy is a {fav_toy}.\n')
print(f'Come meet me today at the {shelter_name}!\n')
print('----------------------------------------')
print(f'Adoption ID: {pet_name}-{pet_type}-{shelter_name}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')