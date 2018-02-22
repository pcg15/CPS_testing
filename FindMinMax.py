def FindMinMax(list_):

    """Returns the tuple of the minimum and maximum of a list of numbers.

    :param list1: List of the numbers that are either int or float

    :returns: The tuple of the minimum and maximum of the given list
    :raises ImportError: error raised if logging module not found
    :raises TypeError: error raised if input is not a list or a tuple
    :raises ValueError: error raised if input has non-numerical values
    """

    import logging
    str_ = logging.DEBUG
    logging.basicConfig(filename="assignment06log.txt", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)
    logging.info('FindMinMax function initiated')
    try:
        import logging
    except ImportError:
        print("Cannot import logging")
        logging.debug('Make sure you have "logging" module.')
    try:
        type1 = [4, 5, 6, 3]
        type(type1) == type(list_)
    except TypeError:
        print("Give a list please!")
        logging.error('You did not give an input of type "list".')
    for x in list_:
        try:
            x = float(x)
        except ValueError:
            print("Give a list with real numbers!")
            logging.error('Your input has some non-numerical\
            and/or nonreal values.')
    try:
        y = list_[1]
    except:
        print("You need more than one number in the list!")
        logging.warning('Give a list or else you will have \
        two equal values in output tuple.')
    Minimum = min(list_)
    Maximum = max(list_)
    tup = (Minimum, Maximum)
    logging.info("FindMinMax function completed successfully")
    return tup
