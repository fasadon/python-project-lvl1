"""Game module calc."""
import random


def rule_of_game():
    """Do this outputs rule of calc game."""
    print('What is the result of the expression?')


def add():
    """Do this number1 + number2.

    Returns:
        result: integre number of operations (number1 + number2)
        question: string 'number1 + number2'
    """
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(number1 + number2)
    question = '{0} + {1}'.format(number1, number2)
    return question, result


def sub():
    """Do this number1 + number2.

    Returns:
        result: integre number of operations (number1 - number2)
        question: string 'number1 - number2'
    """
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(number1 - number2)
    return '{0} - {1}'.format(number1, number2), result


def mul():
    """Do this number1 + number2.

    Returns:
        result: integre number of operations (number1 * number2)
        question: string 'number1 * number2'
    """
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(number1 * number2)
    return '{0} * {1}'.format(number1, number2), result


def game_calc():
    """Do this return to user random expression and result of this expression.

    Returns:
        expression: random string expression
        result: integre number, true result of expression
    """
    expression, result = random.choice([add(), mul(), sub()])
    return expression, result
