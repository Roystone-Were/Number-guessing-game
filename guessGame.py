import random

while True: #used to run indefinetly untill 'break' is met
    random_number = random.randint(1,10) 
    user_input = int(input("Guess a number from 1 to 10: "))

    while user_input != random_number: 
        if user_input < random_number:
            print("Your Guess is Low, Try again")
        
        elif user_input > random_number:
            print("Your guess is High, Try again")

        user_input = int(input("Guess again: ")) #user enters integer again when conditions are not met
        
    print("You Guessed Correctly!")

    play_again = input("Would You Wish to Play Again? (y/n)") #if user guessed correctly, it will prompt for a new game session, or break
    if play_again != "y":
        break
print("Thanks for playing")

