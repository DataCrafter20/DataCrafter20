import random #Generates random numbers by importing the random module.

def number_guessing_game(): #Specifies the number_guessing_game function.
    print("Number Guessing Game!")
    print("You can make five guesses. You get four more guesses for every accurate guess!")
    print("Every level expands the range of numbers.")
    print("Level 1: 0 to 9... Level 10: 0 to 99")
    
    print("Are you ready!?")
    
    level = 1 #Sets the variable level's initial value to 1, which represents the beginning level.
    maximum_level = 10 #Maximum level is set to 10.
    maximum_guesses = 5 #Limits the amount of guesses that can be made in a level to five.
    secret_number = random.randint(0,9) #Creates a secret number at random for the first level, ranging from 0 to 9.
    guesses_remaining = maximum_guesses #Sets the guesses_remaining variable's initial value to the most guesses that are permitted.

    while level<=maximum_level: #Initiates a while loop, which continues to run as long as the level is below or equal to the maximum level.
        print("\n--- level",level,"---")
        print(" Guess a number between 0 and",9+level*10) #Prints the current level's range of numbers.
        print("You have",guesses_remaining,"guesses remaining.")
        
        guess = int(input("Try to guess the number: ")) #Receives the player's guess as input and turns it into an integer.

        if guess==secret_number: #Verifies whether the estimated number and the secret number match.
            print("You succeeded, well done!")
            if level==maximum_level: #Verifies if the present level is the highest possible level.
                print("Well done! You've finished the game and reached Level 10!")
                break #If the player achieves the highest level, the loop ends.
            
            else: #If the player guesses correctly but not at the highest level, executes.
                level +=1 #The level is incresed by one.
                secret_number = random.randint(0, 9+level*10)#creates a new, wider-ranging secret number for the subsequent level. 
                maximum_guesses +=4 #Increases the upper bound on estimates for the subsequent level by a factor of 4.
                guesses_remaining = maximum_guesses #Resets the remaining guesses to the level's new maximum.
                print("Bravo! You've reached Level", level, "!")

        elif guess < secret_number: #Verifies whether the estimate is less than the coded figure.
            print("HINT! Try a higher number.")
            guesses_remaining -=1 #Reduces the number of guesses remaining by 1.
        else: #Carries out the action if the guess exceeds the secret number.
            print("HINT! Try a lower number.")
            guesses_remaining -=1 #Reduces the number of guesses remaining by 1.

        if guesses_remaining ==0: #This determines if the player is out of guesses.
            print("Game Over!!.")
            print("You tried your best but here's the number: ", secret_number)
            print("Try again, don't give up just yet.")
            break #Since the game is done, break the loop.

number_guessing_game() #In order to begin the game, call the function number_guessing_game().
