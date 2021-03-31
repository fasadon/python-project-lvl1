"""Interface for evengames."""
import random

import prompt


def welcome_user():
    """Hello with the user.

    Returns:
        name: string username
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def is_even(number):
    """Check number for even.

    Args:
        number: any integer positive number

    Returns:
        'yes': string if number is evem
        'no': string if number is odd
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def check_answer(result, answer):
    """Compare user answer with correct answer.

    Args:
        number: any integer positive number
        answer: string 'yes' or 'no'

    Returns:
        True: if useranswer is correct
        False: if useranswer is wrong
    """
    return result == answer


def question(number):
    """Ask question about number.

    Args:
        number: any integer positive number
    """
    print('Question: {0}'.format(number))


def wrong_answer(result, answer, name_user):
    """Do this outputs correct answer, if user send wrong answer.

    Args:
        number: any integer positive number
        answer: string 'yes' or 'no'
        name_user: string username
    """
    correct_answer = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
    print(correct_answer.format(answer, result))
    print("Let's try again, {name}!".format(name=name_user))

    
def rule_of_game():
    """Do this outputs rule of even game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    
def answer_user():
    """Do this invites user to write the answer.
    
    Returns:
        answer_user: 'yes' or 'no'
    """    
    answer_user = prompt.string('Your answer: ')
    return answer_user


def random_number():
    """Return this random number."""
    return random.randint(1, 100)


def right_answer():
    """Do this congratulations to user."""
    print('Correct!')


def congratulation(name):
    """Do this when user win game."""
    print('Congratulations, {0}!'.format(name))


def game_even(name_user):
    """Interace game-even.

    Args:
        name_user: string username
    """
    rule_of_game()
    count_correct_answer = 0
    while count_correct_answer < 3:
        number = random_number()
        result = is_even(number)
        question(number)
        answer = answer_user()
        if check_answer(result, answer):
            right_answer()
            count_correct_answer += 1
            continue
        wrong_answer(result, answer, name_user)
        break
    if count_correct_answer == 3:
        congratulation(name_user)
