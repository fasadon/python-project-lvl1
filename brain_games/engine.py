import prompt



def engine(game_brain, rule_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {0}".format(name))
    rule_game()
    count_correct_answer = 0
    while count_correct_answer < 3:
        question, result = game_brain()
        print('Question: {0}'.format(question))
        answer_user = prompt.string('Your answer: ')
        if answer_user == result:
            print('Correct!')
            count_correct_answer += 1
            continue
        correct_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
        print(correct_answer.format(answer_user, result))
        print("Let's try again, {0}!".format(name))
        break
    if count_correct_answer == 3:
        print("Congratulations, {0}!".format(name))

