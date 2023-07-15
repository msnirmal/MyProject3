print ("Welcome to the quiz!!")
print ()
print ("Note: This quiz has many categories")
print()

player_name = input ("Please enter you name: ")
print ()

print ("Categories")
print ("**********")
print ()
print ("1. History")
print ("2. Food")
print ("3. Animals")
print ()
quizcategory = int(input (f"Hi {player_name}!!! please select the quiz category, Example: 1 for History: "))

if (quizcategory == 1):
    print()
    print("Lets play history quiz!!")
    print()
    
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

    question_index +=1 




 
