# Module 5 Homework
# dynomite_dicts
# Prof. James Mertz
# Josue Tiguila Jr.

# Dictionary name Pokedex
pokedex = {}
pokedex['Venosaur'] = 'Grass', 'Poisen'
pokedex['Charizard'] = 'Fire', 'Flying'
pokedex['Blastoise'] = 'Water'

# Show contents of dictionary
print ("Dictionary with Blastoise")
print (pokedex)

#show contents without Blastoise
print ("Dictionary without Blastoise")
pokedex.pop('Blastoise')
print (pokedex)