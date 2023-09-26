def is_armstrong_number(number):
    length = len(str(number))
    return number == sum(int(char) ** length for char in str(number))
