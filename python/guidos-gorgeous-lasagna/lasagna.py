# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here


def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int number of layers.
    :return: int preparation time derived from 'PREPARATION_TIME'.

    Function takes the number of layers the cake has 
    and then returning the preparation time of that cake based on the 'PREPARATION_TIME'.
    """

    return number_of_layers * PREPARATION_TIME


# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(number_of_layers, elapsed_time):
    """Calculate elapsed time in minutes.

    :param number_of_layers: int number of layers that cake has.
    :param elapsed time: int time that elapsed.

    Funtion that takes number_of_layers and elapsed_time then using these parameters to 
    returning total elapsed time.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_time
