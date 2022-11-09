from consts import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('a') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    KeyError: 'a'
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
