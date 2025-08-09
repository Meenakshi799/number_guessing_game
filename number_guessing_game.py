# generate a random number
# loop
#     ask user to guess the number
#     if not valid number 
#     print error
#     if number less than guess
#     print "Too low!"
#     if number greater than guess
#     print "Too high!"
#     else    
#     print "Congratulations! You've guessed the number!"



import random
num=random.randint(1, 100)
while True:
    n=int(input("Guess a number between 1 and 100: "))
    if n < 0 or n > 100:
        print("Not a valid number. Please try again.")
    elif n<num:
        print("Too low!")
    elif n>num:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        break            
        