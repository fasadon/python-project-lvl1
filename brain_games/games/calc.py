

from brain_games.games.even import question, answer_user, random_number, congratulation, welcome_user, right_answer, check_answer, wrong_answer
import random


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def rule_of_game():
    """Do this outputs rule of calc game."""
    print('What is the result of the expression?')


def add():
    """."""
    number1 = random_number()
    number2 = random_number()
    result = number1 + number2
    return '{0} + {1}'.format(number1, number2), result
    

def sub():
    number1 = random_number()
    number2 = random_number()
    result = number1 - number2
    return '{0} - {1}'.format(number1, number2), result
    
    
def mul():
    number1 = random_number()
    number2 = random_number()
    result = number1 * number2
    return '{0} * {1}'.format(number1, number2), result
    

def game_calc(name_user):
    rule_of_game()
    count_correct_answer = 0
    while count_correct_answer < 3:
        expression, result = random.choice([add(), mul(), sub()])
        question(expression)
        answer = answer_user()
        if is_digit(answer) and check_answer(result, int(answer)):
            right_answer()
            count_correct_answer += 1
            continue
        wrong_answer(result, answer, name_user)
        break
    if count_correct_answer == 3:
        congratulation(name_user)
        
        
