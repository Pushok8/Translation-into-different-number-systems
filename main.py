"""
The number_system module: translates the resulting number to the desired encoding.

Module contains one function that translates the specified number by the user from
 the native encoding to the desired final encoding.
"""

from typing import TypeVar

__all__ = ['number_encoding']
__author = '©Pushok8'
int_str = TypeVar('number', str, int)
_NUMBER_SYSTEM = [
    0, 1, 2, 3, 4, 5,
    6, 7, 8, 9, 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]


def _get_decimal(number: int, number_system: int) -> int:
    convenient_encoding_form = str(number)[::-1]
    i: int = 0
    decimal_encoding: int = 0

    for digit in convenient_encoding_form:
        if digit.isdigit():
            decimal_encoding += NUMBER_SYSTEM.index(int(digit)) * number_system ** i
        else:
            decimal_encoding += NUMBER_SYSTEM.index(digit) * number_system ** i
        i += 1

    return decimal_encoding


def _get_binary(number: int, number_system: int) -> int:
    response = []
    cache = [int(number)]
    b = 0

    while cache[b] > 0:
        process = cache[b] // number_system
        b += 1
        cache.append(process)
        remainder = cache[b - 1] % number_system
        if remainder > 9:
            response.append(NUMBER_SYSTEM[remainder])
        else:
            response.append(str(remainder))

    response.reverse()
    response = ''.join(response)

    if response.isalnum():
        return response

    return int(response)


def number_encoding(number: int_str = 0, initial_number_system: int = 10, final_number_system: int = 10) -> int_str:
    """
    number_encoding(number=10, initial_number_system=10, final_number_system=10)

    It transfers from the received data on the number and its number system and returns to another specified number
     system. The maximum number system is 36.
    :param number: number in the number system you specify. The default is 10.
    :param initial_number_system: Native (in which the number is located) number system. The default is 10.
    :param final_number_system: The final (into which the number will be converted) number system. The default is 10.
    :return: number converted from the 'initial_number_system' number system to the 'final_number_system' number system.
    """
    for i in list(str(number)):
        if str(i).isdigit():
            assert NUMBER_SYSTEM.index(
                int(i)) < initial_number_system, 'You entered the number or symbol in the wrong encoding!'
        else:
            assert NUMBER_SYSTEM.index(
                i) < initial_number_system, 'You entered the number or symbol in the wrong encoding!'

    assert final_number_system <= 36, 'Maximum transfer from number system to another number system - 36!'
    assert initial_number_system <= 36, 'Maximum transfer from number system to another number system - 36!'

    if final_number_system == initial_number_system:
        return number
    elif initial_number_system != 10 and final_number_system == 10:
        return _get_decimal(number, initial_number_system)
    elif initial_number_system != 10 and final_number_system != 10:
        return _get_binary(get_decimal(number, initial_number_system), final_number_system)
    else:
        return _get_binary(number, final_number_system)
