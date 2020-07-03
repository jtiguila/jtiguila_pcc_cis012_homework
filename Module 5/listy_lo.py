# Create a list named food with two elements 'rice' and 'beans'.
# Append the string 'broccoli' to food using .append().
# Add the strings 'bread' and 'pizza' to food using .extend().
# Print the first two items in the food list using print() and slicing notation.
# Print the last item in food using print() and index notation.
food = ["rice", "beans"]
food.append("brocolli")
newFood = ["bread", "pizza"]
food.extend(newFood)

print ("\nFirst two items")
print (food[0:2])

print ("\nLast Item")
print (food[len(food)-1])

# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
# Verify that breakfast has 3 elements using the len built-in.
breakString = "eggs,fruit,orange juice"
breakfast = breakString.split(",")
print ("This is the length of breakfast: " + str(len(breakfast)))

# prompts the user for a floating-point value until they enter stop. 
# Store their entries in a list
userInput = ""
listInput = []
sum = 0
average = 0
while True:
    print ("Please Enter a Floating-Point value. Enter 'stop' to end.")
    userInput = input()
    if (userInput == "stop"):
        break
    elif (userInput == ""):
        sum = sum + 0
    else:
        listInput.append(float(userInput))
        sum = sum + float(userInput)

# Sort and print out sort
listInput.sort()
print ("Here is a sorted list of the values you entered")
print (listInput)

# Average, min, and max found and printed out
average = sum / len(listInput)
print ("Average of all the numbers you entered is: " + str(average))
print ("This is the Minimum: " + str(listInput[0]))
print ("This is the Maximum: " + str(listInput[len(listInput)-1]))