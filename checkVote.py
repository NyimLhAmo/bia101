# check if user can vote
# ?get age from input
# ? convert userinput(str)to int()to number
# ?check if user can vote
       # ?if else statement 
       #? if above 18, print("you can vote")
       #? if below 18 print('you cannot vote')


       #1. get user input
userInput = input(' please type your age: ')
#2. convert user input to number
userage = int(userInput)

#3. check if user can vote
if userage >=18:
    print(' you can vote.')
elif userage < 18:
    print('you cannot vote.')
