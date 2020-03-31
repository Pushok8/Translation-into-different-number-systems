# Creator: ©Pushok8.
# Date: 31 March 2020. COVID-19, hello!)
# Edit: 1 April 2020.
# Has changed: add documentation, changed the location of functions.

NUMBER_SYSTEM = [
    0, 1, 2, 3, 4, 5,
    6, 7, 8, 9, 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]


def get_convenient_encoding_form(number):
    arr = []
    # Get the encoding code in a convenient form
    for i in str(number):
        arr.append(i)
    arr.reverse()
    return arr

def get_decimal_numsys_method(number, number_system):  # Decimal method.
    # The method of conversion to the decimal number system is the conversion
    # from any number system to decimal by multiplying the numbers from the end
    # of the number system which is indicated to the power starting from zero.

    convenient_encoding_form = get_convenient_encoding_form(number)
    i = 0
    decimal_encoding = 0

    # Translates from system less than 10 to decimal system.
    for digit in convenient_encoding_form:
        if digit.isdigit():
            decimal_encoding += NUMBER_SYSTEM.index(int(digit)) * number_system ** i
        else:
            decimal_encoding += NUMBER_SYSTEM.index(digit) * number_system ** i
        i += 1

    return decimal_encoding  # Return number in decimal.

def get_binary_numsys_method(number, number_system):  # Binary numeration method.
    # The binary number system is a way to get the binary number system
    # from the decimal system of the number system by dividing by 2 or
    # the number system that was indicated.

    response = []  # The answer will gradually be added here.
    cache = [int(number)]  # Create cache as RAM which will soon be cleansed.
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
    del cache

    if response.isalnum():
        return response

    return int(response)  # Return number in binary or other number system.

def translateToNumSys(number, initial_number_system=10, final_number_system=10):
    '''
    translateToNumSys(number, initial_number_system=10, final_number_system=10)

    Converts from one number system to another. The maximum number system is 36.
    :param number:                number in the number system you specify.
    :param initial_number_system: initial number system of the number. The default is 10.
    :param final_number_system:   finite number system. The default is 10.
    :return:                      integer number converted to the specified number system.
    '''


    # Сhecks to write the number in the correct encoding
    for i in list(str(number)):
        if str(i).isdigit():
            assert NUMBER_SYSTEM.index(
                int(i)) < initial_number_system, 'You entered the number or symbol in the wrong encoding!'
        else:
            assert NUMBER_SYSTEM.index(i) < initial_number_system, 'You entered the number or symbol in the wrong encoding!'

    assert final_number_system <= 36, 'Maximum transfer from number system to another number system - 36!'
    assert initial_number_system <= 36, 'Maximum transfer from number system to another number system - 36!'

    # Just returns what they gave.
    if final_number_system == initial_number_system:
        return number


    if initial_number_system != 10 and final_number_system == 10:  # Translate to decimal number system
        return get_decimal_numsys_method(number, initial_number_system)

    elif initial_number_system != 10 and final_number_system != 10:  # Translate to other number system
        decimalEncodingValues = get_decimal_numsys_method(number, initial_number_system)
        return get_binary_numsys_method(decimalEncodingValues, final_number_system)

    else:  # Translate to binary number system
        return get_binary_numsys_method(number, final_number_system)
