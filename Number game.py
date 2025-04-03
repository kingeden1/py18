import random #importing module
playing = True #intitalaise
number = str(random.randint(10,20)) #random in-built function

print("I will genetrate a number from 10 to 20, and you have to guess the number one digit at a time. " )
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true
while playing:  
    guess = input("Give me yourbest guess! \n") 
    if number ==guess:
        print("You win the game")
        print("The number was",number)
        break

    else:
        print("Your guess isn't quite right, try again. \n")