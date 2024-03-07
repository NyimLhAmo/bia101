# objective :
# create a program that takes in user input 
# and determine if the number is positive or negative or zero 
# ?print : "your number is positive" or ' your number is negative"
# if else 
# print()
# input()


userInput = input()
userInputTpye = type(userInput)
print("The type of user input is;", userInput)


number = float(input("Enter a number : "))


if number > 0:
    print("The number is positive.")
    

elif number < 0:
    print("The number is negative.")

else:
    print("The number is zero.")