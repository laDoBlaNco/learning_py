# task4.py

# IndexError
# Length of list - I can get the length of a list (number of items in the list) or the length
# of a string (number of chars in the string) by using the len() function

states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "South Dakota",
    "North Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]

print(len(states_of_america))
print(states_of_america[49])
# print(states_of_america[50]) # IndexError, nothing at this index beyond the end
# also known as the "off by 1 error"
print(states_of_america[len(states_of_america) - 1])

print()


# dirty_dozen = [
#     "Strawberries",
#     "Spinach",
#     "Kale",
#     "Nectarine",
#     "Apples",
#     "Grapes",
#     "Peaches",
#     "Cherries",
#     "Pears",
#     "Tomatoes",
#     "Celery",
#     "Potatoes",
# ]

fruits = ['strawberries','nectarines','apples','grapes','peaches','cherries','pears']
vegetables = ['spinach','kale','tomatoes','celery','potatoes']
dirty_dozen = [fruits,vegetables] #  a list of two lists (nested lists)
print(dirty_dozen)

