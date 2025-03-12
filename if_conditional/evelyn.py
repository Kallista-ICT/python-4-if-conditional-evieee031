# Ask for the user birth year
birth_year = int(input("Please enter your birth year (e.g.,1990): "))

# Determine the generation based on the user's input
if birth_year >= 1928 and birth_year <= 1945:   # First threshold condition
     generation = 'Silent generation'             # Category for the first condition
elif birth_year > 1945 and birth_year <= 1964:  # Second threshold condition
    generation = 'Baby boomer'                    #Category for second condition
elif birth_year > 1964 and birth_year <= 1980:  # Third threshold condition
    generation = 'Generation x'                   #Category for the third condition
elif birth_year > 1980 and birth_year <= 1996:  # Fourth threshold condition
    generation = 'Generation millenials'          # Category for the fourth condition
elif birth_year > 1996 and birth_year <= 2012:  # Fifth threshold condition
    generation = 'Generation Z '                  # Category for the fifth condition
else :                                          # Default condition for all the other cases
    generation = 'Generation Alpha'             # Default category for all the other conditions
print(f"Your generation is: {generation}") 