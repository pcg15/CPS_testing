def maxFindDiff(list_):

    """Returns the max difference from a list of numbers

    :param inputList: List of input numbers. May be float or int

    :returns: max difference between any two adjacent numbers from list \
    (list[i]-list[i+1])
    :raises ImportError: raises error if math function is not found
    :raises TypeError: raises error if any list element is a string
    :raises ValueError: raises error if input is numerical, but of wrong type
    """

    import logging
    str_ = logging.DEBUG
    logging.basicConfig(filename="assignment06log.txt", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)
    logging.info("MaxDiff function initiated")
    try:
        import math as mt
    except ImportError:
        logging.warning("Unable to find math package")
        print("cant find package (most likely you have not \
        activated your virtual env)")
    diffList = []
    for i in range(len(list_)):
        if i != (len(list_)-1):
            try:
                oneDiff = mt.copysign((list_[i] - list_[i+1]), 1)
            except TypeError:
                logging.warning('Invalid input: data in list \
                is not all numerical')
                print("attemping math operation on non-numerical input")
            except ValueError:
                logging.warning('Invalid input: data in list is of \
                wrong numerical type')
                print("attempting to use an invalid numerical input \
                (e.g., trying to find the square root of a negative number)")
            diffList.append(oneDiff)
    maxxVal = round(max(diffList), 5)
    logging.info("MaxDiff function completed successfully")
    return maxxVal
