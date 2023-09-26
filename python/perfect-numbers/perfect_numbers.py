from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    facs_sum = sum(factors(number)) - number

    if facs_sum == number:
        return "perfect"
    elif facs_sum > number:
        return "abundant"
    else:
        return "deficient"
