"""Interface for evengames."""
import prompt
import random


def welcome_user():
    """Hello with the user.

    Returns:
        name: username
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def is_even(number):
    """Check number for even.

    Args:
        number: any integer number

    Returns:
        'yes': if number is evem
        'no': if number is odd
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def check_answer(number, answer):
    """Compare user answer with correct answer.

    Args:
        number: any integer number
        answer: useranswer for question

    Returns:
        True: if useranswer is correct
        False: if useranswer is wrong
    """
    correct_answer = is_even(number)
    return (lambda answer1, answer2: answer1 == answer2)(correct_answer, answer)


def question(number):
    """Ask question about number.

    Args:
        number: any integer number
    """
    print('Question: {0}'.format(number))


def wrong_answer(number, answer, name_user):
    """Do this outputs correct answer, if user send wrong answer.

    Args:
        number: any integer number
        answer: useranswer for question
        name_user: username
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, is_even(number)))
    print("Let's try again, {name}!".format(name=name_user))


def game_even(name_user):
    """Interace game-even.

    Args:
        name_user: username
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_correct_answer = 0
    while count_correct_answer < 3:
        number = random.randint(1, 100)
        question(number)
        answer_user = prompt.string('Your answer: ')
        if check_answer(number, answer_user):
            print('Correct!')
            count_correct_answer += 1
            continue
        wrong_answer(number, answer_user, name_user)
        break
    if count_correct_answer == 3:
        print('Congratulations, {name}!'.format(name=name_user))