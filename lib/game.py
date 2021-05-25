from .quiz import run_quiz
from .score import get_score
from .db.qualification import create_qualification
from datetime import datetime

def run_game(questions):
    username = input("¿Cuál es su nombre? ")
    result_quiz = run_quiz(questions)
    finish_at = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    score = get_score(result_quiz)

    print('------ End Game ------')
    print(
        '{} tu puntuaje actual es {} y tu fecha de finalización es {}'.format(
            username,
            str(score),
            finish_at
        )
    )

    qualification = (username, score, finish_at)
    print(create_qualification(qualification))
    print('Ya se guardó tu puntuación')
