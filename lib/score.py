def get_score(result):
    score = 0
    for question in result:
        if question['correct']:
            score += 1
    return score

