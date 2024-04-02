#Start of the quiz
print("Welcome to my quiz")

#Option to quit quiz
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

#Welcome Message
print("Good luck and have fun!")

#Score tracking
score=0

#Question one
answer = input("Will I travel first, or go to school first? ")
if answer.lower() == "school":
    print('correct')
    score += 1
else:
    print("incorrect")
    
#Question two
answer = input("Will I take a one year break for coding or art? ")
if answer.lower() == "both":
    print('correct')
    score += 1
else:
    print("incorrect")

#Final score
if score == 1:
    print("You have scored " + str(score) + " question correct")
else:
    print("you have scored " + str(score) + " questions correct")
print(str((score/2)*100) + "%")

#End of quiz
print("the quiz is now over, time for the next game")

#Number guessing game
playing = input("Do you want to play this next game? ")

if playing.lower() != "yes":
    quit()

#Game two welcome message
print("This will be a number guessing game ")
print("Good luck, have fun! ")

#Import random module from python
import random

#Number aquired by user will become the top of range
top_of_range = input("Type a number: ")

#If top_of_range (user entered number) is a digit, top_of_range string = integer(top_of_range)
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

#Error message (greater than zero) will appear and the game will quit
    if top_of_range <= -2:
        print("please type a number greater than zero")
        quit()

#Error message (not a numerical character) will appear and the game will quit
else:
    print("Make sure to use numerical characters next time")
    quit()

#Generating the random number from (0,top_of_range)
rng = random.randint(0, top_of_range)

#Guess tracking
guesses = 0

#Run while loop (if) True
while True:
    guesses += 1
    user_guess = input("make a guess: ")

    #if user guess isdigit = int, else (error) continue
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please make sure to use numerical characters next time")
        continue

    #If correct break the while loop, else (incorrect) continue
    if user_guess == rng:
        print("thats correct! ")
        break

    #Above or below the answer
    elif user_guess > rng:
        print("you were above the number ")
    else:
        print("you were below the number ")

#Won the game
print("you got it in", guesses, "guesses" )

#End of number guessing game
print("the number guessing is now over, time for the next game")

#Option to quit
playing = input("Do you want to play this next game? ")

if playing.lower() != "yes":
    quit()

#Rock paper scissors and welcome message
print("this will be a rock paper scissors ")
print("best of three ")
print("good luck, have fun! ")

#importing random
import random

#win score tracking
user_wins = 0
computer_wins = 0
best_of_three = 0

#Options
options = ["rock", "paper", "scissors"]

#User input
while True:

    #Round one over
    if best_of_three == 1:
        print("two more rounds to go")

    #Round two over
    if best_of_three == 2:
        print("final round!")

    #Who won
    if best_of_three == 3:
        if user_wins > computer_wins:
            print("you won the best of three ")
            break
        elif user_wins < computer_wins:
            print("the computer won the best of three ")
            break
        else:
            print("the game was a draw ")
            break

    #Users imput
    user_input = input("type, rock/paper/scissors or q to quit ").lower()
    if user_input == "q":
        print("goodbye")
        break
    
    #Error message
    if user_input not in options:
        print("error")
        continue

    #Rock = 0, Paper = 1 Scissors = 2
    random_number = random.randint(0,2)

    #Compters pick
    computers_pick = options[random_number]
    print("the computer picked", computers_pick + ".")

    if user_input == "rock" and computers_pick == "scissors":
        print("you won")
        user_wins += 1
        best_of_three += 1
        continue

    elif user_input == "paper" and computers_pick == "rock":
        print("you won")
        user_wins += 1
        best_of_three += 1

    elif user_input == "scissors" and computers_pick == "paper":
        print("you won")
        user_wins += 1
        best_of_three += 1

    elif user_input == "rock" and computers_pick == "rock":
        print("draw")
        best_of_three += 1

    elif user_input == "paper" and computers_pick == "paper":
        print("draw")
        best_of_three += 1

    elif user_input == "scissors" and computers_pick == "scissors":
        print("draw")
        best_of_three += 1

    else:
        print("you lost")
        computer_wins += 1
        best_of_three += 1
        continue
    
#The score
print("you won", user_wins, "times")
print("the computer won", computer_wins, "times")

#End of rock paper scissors
print("rock paper scissors is now over, time for the next game ")

#Option to quit
playing = input("Do you want to play this next game? ")

if playing.lower() != "yes":
    quit()

#Choose your own adventure welcome message
print("this will be a choose your own adventure style game ")
print("good luck, have fun! ")

name = input("type your name ")
print("welcome", name, "to this adventure ")

answer = input("you are on a dirt road, it has coe to an end and you can go left or right. which way woukd you like to go? ").lower()

if answer == "left":
    print("You chose the dangerous path")
elif answer == "right":
    print("You chose a scenic and peaceful path")

#End of the game, Hope you had fun
print("That is the end of game, I hope you had fun. This was a great learning expreience and really jump started me into learning how to code.")
