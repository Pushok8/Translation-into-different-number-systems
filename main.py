# Creator: ©Pushok8.
# Date: 31 March 2020. COVID-19, hello!)

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


def number_system_translation(number, initial_encoding, final_encoding):
    # Сhecks to write the number in the correct encoding
    for i in list(str(number)):
        if str(i).isdigit():
            assert NUMBER_SYSTEM.index(
                int(i)) < initial_encoding, 'You entered the number or symbol in the wrong encoding!'
        else:
            assert NUMBER_SYSTEM.index(i) < initial_encoding, 'You entered the number or symbol in the wrong encoding!'

    assert final_encoding <= 36, 'Maximum transfer from number system to another number system - 36!'
    assert initial_encoding <= 36, 'Maximum transfer from number system to another number system - 36!'

    # Just returns what they gave.
    if initial_encoding == final_encoding:
        return number

    def get_decimal_encoding(number):  # Decimal number system
        convenient_encoding_form = get_convenient_encoding_form(number)
        i = 0
        decimal_encoding = 0

        # Translates from system less than 10 to decimal system.
        for digit in convenient_encoding_form:
            if digit.isdigit():
                decimal_encoding += NUMBER_SYSTEM.index(int(digit)) * initial_encoding ** i
            else:
                decimal_encoding += NUMBER_SYSTEM.index(digit) * initial_encoding ** i
            i += 1

        return decimal_encoding  # Return number in decimal.

    def get_binary_encoding(number):  # Binary number system
        response = []  # The answer will gradually be added here.
        cache = [int(number)]  # Create cache as RAM which will soon be cleansed.
        b = 0

        while cache[b] > 0:
            process = cache[b] // final_encoding
            b += 1
            cache.append(process)
            remainder = cache[b - 1] % final_encoding
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

    if initial_encoding != 10 and final_encoding == 10:  # Translate to decimal number system
        return get_decimal_encoding(number)

    elif initial_encoding != 10 and final_encoding != 10:  # Translate to other number system
        decimal_encoding_values = get_decimal_encoding(number)
        return get_binary_encoding(decimal_encoding_values)

    else:  # Translate to binary number system
        return get_binary_encoding(number)
