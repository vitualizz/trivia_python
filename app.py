#!/bin/python3

from lib.questions import get_questions
from lib.game import run_game

def main():
    questions = get_questions('quizzes.txt')
    run_game(questions)


if __name__ == '__main__':
    main()
