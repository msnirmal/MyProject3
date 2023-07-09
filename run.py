print ("Welcome the quiz!!")
print ("This is a general knowledge quiz")

player_name = input ("Please enter you name: ")
playquiz = input (f"{player_name},Do you want to play the quiz?: ")
if playquiz == "yes":
    print ("Lets play!!!!")
     
else:
    quit()
questions = ("What's national bird of India? " ,
             "What's the national sport of India?" ,
             "What's the national Animal of India? "
            )

options = (("1. Peacock", "2. Pigeon", "3. Swan" ),
           ("1. Football", "2. Cricket", "3. Hockey"),
           ("1. Lion", "2. Tiger", "3. elephant"))

answers = ("Peacock", "Hockey", "Tiger")

score = 0
question_index = 0

 
for question in questions: 
    print(question)

    for option in options[question_index]:
        print(option)
    guess = input ("Enter your answer: ")
    if guess == answers [question_index]:
        score += 1
        print ("Correct ")
    else:
        print("Incorrect")
    question_index += 1
 


    





 



