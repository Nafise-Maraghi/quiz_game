import json
import random
import requests


def get_question():
    my_request = requests.get("https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple")
    if my_request.status_code != 200:
        print("Something went wrong. Please try again later.")
        return False

    question_details = my_request.text
    question_details = json.loads(question_details)
    question_text = question_details["results"][0]["question"]
    correct_answer = question_details["results"][0]["correct_answer"]
    answers = question_details["results"][0]["incorrect_answers"]
    answers.append(correct_answer)
    random.shuffle(answers)

    return [question_text, answers, correct_answer]


def print_question(question, answers):
    print("\n" ,question, "\n")
    for i in range(len(answers)):
        print("  " , i + 1 ,". ", answers[i])


def get_answer(answers, correct_answer):
    status = True
    while status == True:
        user_answer = input("\nEnter the number of the correct answer: ")
        try:
            user_answer = int(user_answer)
            if user_answer >= 1 and user_answer <= 4:
                if answers[user_answer - 1] == correct_answer:
                    print("\nCorrect!")
                else:
                    print("\nIncorrect!")
                    print("The correct answer is: " ,correct_answer)
                status = False
            else:
                print("\nInvalid input")
                continue
        except:
            print("\nInvalid input")
            continue


def continue_or_quit():

    status = True
    while status == True:
        user_input = input("\nPress inter to continue or \"Q\" to quit: ")
        if user_input.lower() == "q":
            print("\nComeback soon!\n")
            return False
        elif user_input == "":
            return True
        else:
            print("\nInvalid input")
            continue



flag = True
question_store = list() 

while flag == True:
    get_question_return = get_question()
    if get_question_return == False: # means that my_question.status_code != 200. line 8
        break

    question = get_question_return[0]
    if question in question_store:  # skips repetitive questions
        continue
    else:
        question_store.append(question)

    answers = get_question_return[1]
    correct_answer = get_question_return[2]
    print_question(question, answers)
    get_answer(answers, correct_answer)
    flag = continue_or_quit()
