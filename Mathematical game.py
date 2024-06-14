import random #Import the random module.

def generate_sum(level): #Define a function generate_sum with a parameter level.
    x = random.randint(-5*level,5*level) #Generate a random integer for x.
    y = random.randint(-5*level,5*level) #Generate a random integer for y.
    operator = random.choice(["+","-","*","/"]) #Choose a random operator.
    if operator=="/" and y==0: #Check if division by zero.
        return generate_sum(level)
    print("What is the answer of:", x, operator , y ,"?") #Print the equation.
    return x,y,operator

def check_answer(x, y, operator,ans): #Define a function check_answer.
    if operator=="+":
        return x+y == ans
    elif operator=="-":
        return x-y== ans
    elif operator=="*":
        return x*y==ans
    elif operator=="/":
        return x/y==ans

def play_the_game():  #Define a function play_the_game.
    level=1
    accurate_answers=0
    while level <= 5:
        x,y,operator = generate_sum(level)
        user_answer = float(input("Enter your answer or quit(q): "))#Get user input.
        if user_answer == 'q': #Check if the user wants to quit.
            break
        if check_answer(x,y,operator,user_answer): #Check if the answer is correct.
            accurate_answers+= 1 #Increment correct answers count.
            print("Correct!")
            if accurate_answers %5 == 0: # Check if level up is needed.
                level+= 1 #Increase the level.
        else: #If answer is incorrect.
            print("Game over!") #Print game over message.
            break
    print("Thanks for playing!") #Print thanks message.

play_the_game() #Calls the function play_the_game.