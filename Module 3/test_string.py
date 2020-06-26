# Print a string that uses double quotation marks inside the string.
dubQuotes  = 'He said, "Hello World"'
print (dubQuotes)

# Print a string that uses an apostrophe inside the string.
apostString = "Caesar's Palace"
print (apostString)

# Print a string that spans multiple lines, with white space preserved
WhiteSpacePreserveString = """Top is feeding. But it's ok, because
    our bot is fed and will carry.
"""
print (WhiteSpacePreserveString)

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