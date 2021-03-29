"""Interface for braingames."""


import prompt


def welcome_user():
    """Hello with the user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
