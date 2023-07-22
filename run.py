import time
import os

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

def clear():
    """
    Function to clear the terminal on windows, mac and
    linux for a better user experience.
    """
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Mac and Linux (here, os.name is 'posix')
    else:
        os.system('clear')


player_name = input ("Please enter your name or press enter: \n")
time.sleep(3)
clear()
print(f"Welcome {player_name}!! lets play the quiz")
time.sleep(3)
clear()
print ("Here are your questions, wish you all the best")
time.sleep(3)
clear()

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1 

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)               
        if guess == "A":
            correct_guesses += 1
        elif guess == "B":
            correct_guesses += 1
        elif guess == "C":
            correct_guesses += 1
        elif guess == "D":
            correct_guesses += 1
        else:
            print ("invalid")
        guess = input("Enter (A, B, C, or D): ")
        correct_guesses += check_answer(questions.get(key), guess)
        time.sleep(3)
        clear()
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):  

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        time.sleep(2)
        clear()
        return True
    else:
        return False

new_game()    

while play_again():
    new_game()

print("Byeeeeee!")
