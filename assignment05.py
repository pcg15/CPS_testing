def main(list1, list2, list3):

    """Program that when given a list will return the sum of the list, \
    a tuple of the min and max from the list, and the maximum difference \
    between two adjacent numbers in the list.

    :param list: Input that is a list of numbers. Can be integers or \
    floats

    :returns: combined sum of a list of numbers
    :returns: a tuple of the min and max from the list
    :returns: the maximum difference between two adjacent numbers in the list
    :raises ImportError: an error is raised if numpy cannot be found
    :raises TypeError: an error is raised if the data input contains \
    combined data types or a string instead of integers or a list
    :raises ValueError: an error is raised if the data input contains \
    unsupported numerical values (i.e. an imaginary number or string)
    """
    import logging
    import math
    db_str1 = logging.DEBUG
    logging.basicConfig(filename="assignment05log.txt", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=db_str1)
    logging.info("Beginning of assignment05")
    print("Max Difference is: " + str(maxFindDiff(list1)))
    logging.info("Assignment05: Maximum difference found")
    print("Summation Total is: " + str(summation(list2)))
    logging.info("Assignment05: Sum of list numbers completed")
    print("FindMinMax: " + str(FindMinMax(list3)))
    logging.info("Assignment05: The maximum and minimum were found")
    logging.info("Assignment 05 program completed successfully")


def maxFindDiff(list1):
    from maxDifference import maxFindDiff
    out1 = maxFindDiff(list1)
    return out1


def summation(list2):
    from summation import summation
    out2 = summation(list2)
    return out2


def FindMinMax(list3):
    from FindMinMax import FindMinMax
    out3 = FindMinMax(list3)
    return out3


if __name__ == '__main__':
    main()
