#Module 4 Homework
#Mathematical.py
#Prof. James Mertz
#Josue Tiguila Jr

# Two Variable; different way of saving 25,000,000
underNum = 25_000_000 
num1 = 25000000

# Print out variables above with variable name
underString = "underNum: {}"
numString = "num1: {}"
print (underString.format(underNum))
print (numString.format(num1))

# Creat var with 175000.0 in Scientific Notation and Print it
num2 = 1.75e5
print (num2)

# Calculate exponet and print out the answer
print("Welcome to Exponent calculator")
print("Please enter the base")
baseNum = int(input())
print("Please enter the exponent")
expNum = int(input())
answerNum = baseNum ** expNum
outString = "{} to the power of {} = {}"
print(outString.format(baseNum, expNum, answerNum))