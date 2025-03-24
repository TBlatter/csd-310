#Tyson Blatter 2-8-25 6.2
#this is code that will create a tuple and utilize it to create outputs
#creating values for my tuple
pokemon_tuple = (
        "Eevee", "Umbreon", "Espeon", "Snorlax", "Mewtwo", "Dragonite",
    "Lucario", "Garchomp", "Greninja", "Infernape", "Togekiss",
    "Rayquaza", "Umbreon", "Sylveon", "Metagross", "Tyranitar", "Jirachi", "Rockruff"
)

# This code is to display the content in a single statement
print("Pokemon Tuple Contents:", pokemon_tuple)

#This code uses each value in a complete sentence
print("\nList of different Pokémon:")
for pokemon in pokemon_tuple:
    print(f"{pokemon} is a popular Pokémon loved by many adoring trainers!")

#this is the same tuple in a reversed order with a new context
print("\nReversed Pokémon List with a new meaning:")
for pokemon in reversed(pokemon_tuple):
    print(f"If you had {pokemon} on your team, you would be unstoppable!")