#!/bin/python3
import random

TOTAL_QUESTIONS=10

def get_questions(filepath):
    questions = []
    with open(filepath) as file:
        identifier = 0
        count_lines = 0
        quiz = {}
        for line in file:
            count_lines += 1
            identifier += 1
            line = line.strip()

            quiz['id'] = identifier
            if count_lines == 1:
                quiz['question'] = line
            elif count_lines == 2:
                quiz['answer'] = line
            elif count_lines in [3, 4, 5, 6]:
                if 'options' in quiz:
                    quiz['options'].append(line)
                else:
                    quiz['options'] = [line]

                if count_lines == 6:
                    questions.append(quiz)
                    count_lines = 0
                    quiz = {}
            
    return randomize_questions(questions)


def randomize_questions(questions):
    r_questions = []
    count_questions = 0
    while count_questions < TOTAL_QUESTIONS:
        number_quiz = random.randrange(len(questions))
        r_question = questions[number_quiz]
        r_question_ids = [quiz['id'] for quiz in r_questions]
        if r_question['id'] not in r_question_ids:
            count_questions = len(r_questions)
            r_questions.append(r_question)
    return r_questions
