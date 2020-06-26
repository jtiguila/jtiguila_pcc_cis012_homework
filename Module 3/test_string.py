# Module 3 Homework
# test.string.py
# Instructor James Mertz
# By Josue Tiguila Jr.

# Print a string that uses double quotation marks inside the string.
dubQuotes  = 'He said, "Hello World"'
print (dubQuotes)

# Print a string that uses an apostrophe inside the string.
apostString = "Caesar's Palace"
print (apostString)

# Print a string that spans multiple lines, with white space preserved
whiteSpacePreserveString = """Top is feeding. But it's ok, because
    our bot is fed and will carry.
"""
print (whiteSpacePreserveString)

# Print a string that is coded on multiple lines but displays on a single line.
singleLineString = "Raze is OP. \
She has 3 spells that deal damage. \
Last game she got an ACE without shooting her gun."    
print(singleLineString)

# Create a string and print its length
lengthString = "It is good that Void out taken out. It was hard to balance."
print (len(lengthString))

# Create two strings, concatenate them, and print the result
firstString = "This is the First half "
secondString = "and this is the Second half."
togetherString = firstString + secondString
print (togetherString)

# Create two string and use concatenation to add a space in-between them and print the result
beginString = "This is the beginning"
endString = "and this is the end"
togetherString2 = (beginString + " " + endString)
print (togetherString2)

# Print the sub-string 'nerf' from the string 'nerf herder'
nerfString = "nerf harder"
subNerf = nerfString[0:4]
print (subNerf)

#Convert the following strings to lower case:
#Jalin, Obi-Wan, Darth Maul, Rex
jalinString = "Jalin"
print (jalinString.lower())
obiString = "Obi-Wan"
print (obiString.lower())
maulString = "Darth Maul"
print (maulString.lower())
rexString = "Rex"
print (rexString.lower())

#Convert the following strings to upper case:
#Jalin, Obi-Wan, Rex
print (jalinString.upper())
print (obiString.upper())
print (rexString.upper())

#Remove whitespace from the following strings:
ezraString = " Ezra Bridger is my apprentice! "
print (ezraString.strip())

#Replace 'Han' with 'Ben', and 'shot' with 'stabbed' in the following string:
hanString = "Han Solo shot first"
print (hanString.replace('Han', 'Ben').replace('shot', 'stabbed'))

#Find the location of the string 'Night' within the following string. 
# Then print out the start and end index of that string along with the actual substring:
dathomirString = "Dathomir is the home planet of the Night Sisters"
locationNight = dathomirString.find('Night')
print ("Start Index: " + str(locationNight))
print ("End Index: " + str(locationNight+6))
print (dathomirString[locationNight:locationNight+6])

#Using formatted strings, create the following template and store it in a variable:
#Using the variable from before and the .format method, insert the ship name "Millennium Falcon" and distance of 12
#Using an fstring and the same template above, insert the ship name "Ghost" and distance of 20
ship = "Milenium Falcon"
distance = "12"
print ("The {} can make the Kessel Run in less than {} parsecs".format(ship, distance))
ship = "Ghost"
distance = "20"
print (f"The {ship} can make the Kessel Run in less than {distance} parsecs")