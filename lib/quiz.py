LETTERS = ['A', 'B', 'C' , 'D']

def run_quiz(questions):
    result_quiz = []
    for quiz in questions:
        print(quiz['question'])

        for index, option in enumerate(quiz['options']):
            print(LETTERS[index] + "). " + option)

        answer = input('¿Cuál es tu respuesta? ').upper()
        while valid_answer(answer) is False:
            print("Ingresa una respuesta válida.")
            answer = input('¿Cuál es tu respuesta? ').upper()

        correct = (quiz['answer'].upper() == answer)
        print("Su respuesta es {}".format('Correcta' if correct else 'Incorrecta'))

        result = {}
        result['id'] = quiz['id']
        result['correct'] = correct

        result_quiz.append(result)
    return result_quiz


def valid_answer(answer):
    return answer in LETTERS
