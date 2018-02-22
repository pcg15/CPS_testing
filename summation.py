def summation(list_):

    """Returns the sum of a list of numbers

    :param list_: Input that is a list of numbers. Can be integers or \
    floats

    :returns: combined sum of a list of numbers
    :raises ImportError: an error is raised if numpy cannot be found
    :raises TypeError: an error is raised if the data input contains \
    combined data types or a string instead of integers or a list
    :raises ValueError: an error is raised if the data input contains \
    unsupported numerical values (i.e. an imaginary number or string)
    """

    import logging
    str_ = logging.DEBUG
    logging.basicConfig(filename="assignment06log.txt", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)
    logging.info("Summation function initiated")
    try:
        import numpy as np
        import math
    except ImportError:
        logging.warning("Not able to find package numpy")
        print("ImportError:")
        print("Numpy not found. Ensure virtual environment activated.")
    try:
        sum_list_ = np.sum(list_)
    except TypeError:
        logging.warning("Invalid input: list contains data that mixes types \
        or that is not numerical")
        print("TypeError:")
        print("Your input is not a list or integer. Make ammends accordingly.")
    except ValueError:
        logging.warning("Invalid input: list contains data that is not of the \
        correct numerical type")
        print("ValueError")
        print("Your input is not a valid number. Try again.")
    sum_list_ = np.sum(list_)
    logging.info("Summation function completed successfully")
    return sum_list_
