#This simple program gets a json file to generate the questions, shows it to the user and asks her 
#for an answer, if the user checks it and thinks its correct annotates one point to the score 

import json
JSON_PATH = "to-study.json"

#TODO - Read a json file
def read_json(filepath):

    with open(filepath, "r", encoding="utf-8") as q_file:
        questions = json.load(q_file)

    return questions

#TODO - Create a list of questions
def create_question_list(q_dict):

    question_list = []
    for question, answer in read_json(q_dict).items():
        question_list.append((question, answer))

    return question_list

#TODO - Create the user and the score
print("What's your name?:")
user_name = input(">")
user_score = 0

print(f"Hello {user_name} your max. score is {user_score}")

#TODO - Loop to answer the questions to the user and get the user guess
while True:
    for question, answer in create_question_list(JSON_PATH):
        print("/////////////")
        print("Pregunta...")
        print(question)
        user_guess = input(">")


#TODO - Show comparison between guessed and correct answer
        print("The correct answer was: ")
        print(answer)

#TODO - Ask the user if it was correct and update the score
        print("Was your guess correct? (y/n)")
        user_choice = input(">").lower()
        if user_choice == "y" or user_choice == "yes":
            user_score += 1

#TODO - At the end print the score
    print(f"Your current score is {user_score}")

#TODO - Ask the player if she wants to play again
    print("Do you want to play again?")
    user_choice = input(">")
    if user_choice == "y" or user_choice == "yes":
        continue
    else:
        print(f"Goodbye {user_name}")
        break
