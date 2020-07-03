# Module 5 Homework
# loopy_loops.py
# Prof. James Mertz
# Josue Tiguila Jr.

# Tuple named pokemon that holds strings 'picachu', 'charmander', and 'bulbasaur'.
# Print string located at index[1] 
# Values of pokemon unpacked in to starter1, starter2, starter3.
pokemon = ('picachu', 'charmander', 'bulbasur')
print (pokemon[1])
starter1, starter2, starter3 = pokemon
print (starter1)
print (starter2)
print (starter3)

# Tuple with my name
# check how "i's" are in my name
myName = "Josue Tiguila Jr"
print ("How Many 'i's in my name")
print (tuple(myName).count('i'))

# Forr loop print 2 - 10
print ("\nFor Loop")
x = range(9)
for n in x:
  print(n+2)

# while loop prints 2 - 10
print ("\nWhile loop")
i = 0
while (i < 9):
  print (i+2)
  i = i + 1

# Write a for loop that iterates over the string 'This is a simple string' and prints each character.
print ("\nSimple String")
simpString = 'This is a simple string'
for j in simpString:
  print(j)

# Using a nested for loop, iterate over the following set ('this', 'is', 'a', 'simple', 'set') and print each word, three times.
print ("\nSimple Set")
simpSet = ('this', 'is', 'a', 'simple', 'set')
k = 0
m = 0
for k in simpSet:
  for m in range (0,3):
    print (k)
    # m = m + 1