""""Game module."""

import random


def rule_of_game():
    """Do this outputs rule of calc game."""
    print('What is the result of the expression?')


def add():
    """."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = number1 + number2
    return '{0} + {1}'.format(number1, number2), str(result)
    

def sub():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = number1 - number2
    return '{0} - {1}'.format(number1, number2), str(result)
    
    
def mul():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = number1 * number2
    return '{0} * {1}'.format(number1, number2), str(result)
    

def game_calc():
    expression, result = random.choice([add(), mul(), sub()])
    return expression, result
        
        
