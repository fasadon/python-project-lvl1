"""Game module gcd."""
import random
from collections import Counter
from functools import reduce


def rule_of_game():
    """Do this outputs rule of gcd game."""
    print('Find the greatest common divisor of given numbers.')


def primfacs(number):
    """Do this break it up number for prime numbers.

    Args:
        number: any itegre number

    Returns:
        primfac: list prime numbers
    """
    prime_number = 2
    primfac = []
    while prime_number * prime_number <= number:
        while number % prime_number == 0:
            primfac.append(prime_number)
            number = number / prime_number
        prime_number = prime_number + 1
    if number > 1:
        primfac.append(int(number))
    return primfac


def gcd(number1, number2):
    """Find greatest common divisor.

    Args:
        number1: any integre number
        number2: any integre number

    Returns:
        result: integre number
    """
    lst_gcd = []
    dict_primfacs_number1 = Counter(primfacs(number1))
    dict_primfacs_number2 = Counter(primfacs(number2))
    for key, value in dict_primfacs_number1.items():
        if key in dict_primfacs_number2:
            value2 = dict_primfacs_number2.get(key)
            if value < value2:
                lst_gcd.append(key**value)
            else:
                lst_gcd.append(key**value2)
    if not lst_gcd:
        return 1
    result = reduce(lambda x, y: x * y, lst_gcd)
    return result


def game_gcd():
    """Use this to two random numbers return them greatest common divisor.

    Returns:
        question: string 'number1 number2'
        result: string integre number,gcd of number1 and number2
    """
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)
    question = '{0} {1}'.format(number1, number2)
    result = str(gcd(number1, number2))
    return question, result
