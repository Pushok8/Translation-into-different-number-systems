"""
The number_system module: translates the resulting number to the desired encoding.

Module contains one function that translates the specified number by the user from
 the native encoding to the desired final encoding.
"""

from typing import TypeVar

__all__ = ['number_encoding']
__author = '©Pushok8'
int_str = TypeVar('number', str, int)
_NUMBER_SYSTEM = (
    0, 1, 2, 3, 4, 5,
    6, 7, 8, 9, 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
)


def _get_decimal(number: int, number_system: int) -> int:
    convenient_encoding_form = str(number)[::-1]
    i: int = 0
    decimal_encoding: int = 0

    for digit in convenient_encoding_form:
        if digit.isdigit():
            decimal_encoding += _NUMBER_SYSTEM.index(int(digit)) * number_system ** i
        else:
            decimal_encoding += _NUMBER_SYSTEM.index(digit) * number_system ** i
        i += 1

    return decimal_encoding


def _get_binary(number: int_str, number_system: int) -> int:
    response = []
    cache = [int(number)]
    b = 0

    while cache[b] > 0:
        process = cache[b] // number_system
        b += 1
        cache.append(process)
        remainder = cache[b - 1] % number_system
        if remainder > 9:
            response.append(remainder)
        else:
            response.append(str(remainder))

    response.reverse()
    response = ''.join(response)

    if str(response).isalnum():
        return response

    return int(response)


def number_encoding(number: int_str = 0, initial: int = 10, final: int = 10) -> int_str:
    """
    number_encoding(number=10, initial=10, final=10)

    It transfers from the received data on the number and its number system and returns to another specified number
     system. The maximum number system is 36.
    :param number: number in the number system you specify. The default is 10.
    :param initial: Native (in which the number is located) number system. The default is 10.
    :param final: The final (into which the number will be converted) number system. The default is 10.
    :return: number converted from the 'initial' number system to the 'final' number system.
    """
    for i in list(str(number)):
        if str(i).isdigit():
            assert _NUMBER_SYSTEM.index(
                int(i)) < initial, 'You entered the number or symbol in the wrong encoding!'
        else:
            assert _NUMBER_SYSTEM.index(
                i) < initial, 'You entered the number or symbol in the wrong encoding!'

    assert final <= 36, 'Maximum transfer from number system to another number system - 36!'
    assert initial <= 36, 'Maximum transfer from number system to another number system - 36!'

    if final == initial:
        return number
    elif initial != 10 and final == 10:
        return _get_decimal(number, initial)
    elif initial != 10 and final != 10:
        return _get_binary(_get_decimal(number, initial), final)
    else:
        return _get_binary(number, final)
