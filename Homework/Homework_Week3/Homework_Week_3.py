# TASK 1 (Conditional flow)

# Question 1

weather_check = input('Is it raining? y/n ').lower()
if weather_check == 'y':
   print("Take an umbrella")
elif weather_check == 'n':
   print('You don\'t need an umbrella')
else:
   print('Invalid option')

# Question 2

'''
Answer:
I fixed the syntax by adding the missing underline to the variable boat_cost, 
by adding the closing parentheses to the second print statement, 
and converting the input into an integer using the built-in function int() 
so Python can evaluate the condition inside the If statement to check the budget.

'''
my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money < boat_cost:
   print('You can afford the boat hire')
else:
   print('You cannot afford the boat hire')

# Question 3
# I couldn't figure out how to get to the decades :(

def check_century(year):
   if year >= 1800 and year <= 1899:
      century = "Nineteenth century"
   elif year >= 1900 and year <= 1950:
      century = "Twentieth century"
   else:
      print("Sorry, century not found.")

   return century

input_year = int(input(" In what year was the book published? "))
century = check_century(input_year)


# TASK 2 (Lists and Dictionaries)
# Question 1

# Answer:
# The index in Python starts from 0, not 1. So, to find the first element of the list you should print:

shopping_list = [
	"oranges",
	"cat food",
	"sponge cake",
	"long-grain rice",
	"cheese board",
]
print(shopping_list[0])


# Question 2

chocolates = {

   'milk': 1.20,

   'white': 1.50,

   'dark': 1.80,

   'vegan': 2.00,

}

item_price = input("What is the item? ")

print(f'The price is: {chocolates[item_price]}')

# Question 3


def lottery_ticket():
    numbers_list = []
    for i in range(7):
        numbers_list.append(random.randint(1, 50))
    return numbers_list


def compare_list(numbers_list, winning_numbers):
    matches = set(winning_numbers).intersection((numbers_list))
    match_num = len(matches)
    if match_num == 3:
        prize = 20
    elif match_num == 4:
        prize = 40
    elif match_num == 5:
        prize = 100
    elif match_num == 6:
        prize = 10000
    elif match_num == 7:
        prize = 1_000_000
    else:
        prize = None
    return prize


winning_numbers = [37, 11, 19, 32, 46, 39, 22]
numbers_list = lottery_ticket()
results = compare_list(numbers_list, winning_numbers)

if results:
    print(f'You won: $ {results}.')
else:
    print('Maybe next time!')

# TASK 3 (Read and Write files)

# Question 1

'''
Answer:

PIP is a package manager used to install libraries that other people have written. 
It simplifies the installation and management of modules and packages 
that are not part of the Python standard library.

'''

# Question 2

''' 
Answer: 
To write and save data into a file, it’s necessary to use the mode ‘w’ 
that stands for writing, instead of ‘r’ that stands for ‘reading’. 
'''

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
	poem_file.write(poem)

# Question 3

song = """You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use

And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away

Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind

I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)"""

with open('song.txt', 'w') as song_file:
    song_file.write(song)

with open('song.txt', 'r') as song_file:
    for line in song_file.readlines():
        if 'still' in line:
            print(line)

# TASK 4 (API)

# Question 1

import requests


def get_pokemon_name(pokemon_id):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon_name = response.json()["name"]
    return pokemon_name

pokemon_ids = [1, 2, 3, 4, 5, 6]

pokemon_names = []
for pokemon_id in pokemon_ids:
    pokemon_name = get_pokemon_name(pokemon_id)
    pokemon_names.append(f'{pokemon_name}\n')

with open('pokemons.txt', 'w') as file:
    file.writelines(pokemon_names)