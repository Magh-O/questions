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

#TODO - Loop to answer the questions to the user and get the user guess

#TODO - Show comparison between guessed and correct answer

#TODO - Ask the user if it was correct and update the score

#TODO - At the end print the score
