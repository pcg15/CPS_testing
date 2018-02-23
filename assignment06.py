import logging
import math
str_ = logging.DEBUG
logging.basicConfig(filename="assignment06log.txt", format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)


class Assignment06:

    """Program that when given a list will return the sum of all list \
    compoenents, a tuple of the minimum and maximum values from the list, \
    and the maximum difference found between two adjacent numbers in the list.

    :param list: Input that is a list of numbers. Can be integers or \
    floats

    :returns Sum: combined sum of a list of numbers

    :returns MinMax: a tuple of the min and max from the list

    :returns MaxDifference: the maximum difference between two adjacent \
    numbers in the list
    :raises ImportError: an error is raised if necessary functions cannot be \
    found
    :raises TypeError: an error is raised if the data input contains \
    combined data types or a string instead of integers or a list
    :raises ValueError: an error is raised if the data input contains \
    unsupported numerical values (i.e. an imaginary number or string)
    """

    def __init__(self, list_=[1, 5, 6, 7]):
        self.list_ = list_
        self.Sum = None
        self.FindSummation()
        self.MinMax = None
        self.FindMinMax()
        self.MaxDiff = None
        self.FindMaxDifference()

    def FindSummation(self):
        """function to sum the components of a list

        :returns: the sum of the complete list
        :param: list components can be a float or integer
        """

        try:
            from summation import summation
            logging.info("Assignment06: summation was imported successfully")
        except:
            print("ImportError:")
            print("Summation function could not be found")
        try:
            self.Sum = summation(self.list_)
            logging.info("Assignment06: Sum attribute assigned to list_")
        except TypeError:
            logging.warning("Invalid input: list contains data that mixes \
            types or that is not numerical")
            print("TypeError:")
            print("Your input is not a list or integer. Make ammends \
            accordingly.")
        except ValueError:
            logging.warning("Invalid input: list contains data that is not of \
            the correct numerical type")
            print("ValueError")
            print("Your input is not a valid number. Try again.")
        logging.debug("Assignment06: Sum = " + str(summation(self.list_)))

    def FindMinMax(self):
        """function that finds the minimum and maximum values in a list

        :returns: the minimum and maximum values as a tuple
        :param: list components can be a float or integer
        """

        try:
            from FindMinMax import FindMinMax
            logging.info("Assignment06: FindMinMax was imported successfully")
        except:
            print("ImportError:")
            print("FindMinMax function could not be found")
        try:
            self.MinMax = FindMinMax(self.list_)
            logging.info("Assignment06: MinMax attribute assigned to list_")
        except TypeError:
            logging.warning("Invalid input: list contains data that mixes \
            types or that is not numerical")
            print("TypeError:")
            print("Your input is not a list or integer. Make ammends \
            accordingly.")
        except ValueError:
            logging.warning("Invalid input: list contains data that is not of \
            the correct numerical type")
            print("ValueError")
            print("Your input is not a valid number. Try again.")
        logging.debug("Assignment06: MinMax = " + str(FindMinMax(self.list_)))

    def FindMaxDifference(self):
        """function that finds the maximum difference between two numerical \
        components of a list

        :returns: the maximum difference found between two components of a \
        numerical list
        :param: list components can be a float or integer
        """
        try:
            from maxDifference import maxFindDiff
            logging.info("Assignment06: maxFindDiff was imported successfully")
        except:
            print("ImportError:")
            print("FindMinMax function could not be found")
        try:
            self.MaxDiff = maxFindDiff(self.list_)
            logging.info("Assignment06: MaxDiff attribute assigned to list_")
        except TypeError:
            logging.warning("Invalid input: list contains data that mixes \
            types or that is not numerical")
            print("TypeError:")
            print("Your input is not a list or integer. Make ammends \
            accordingly.")
        except ValueError:
            logging.warning("Invalid input: list contains data that is not of \
            the correct numerical type")
            print("ValueError")
            print("Your input is not a valid number. Try again.")
        logging.debug("Assignment06: MinMax = " + str(maxFindDiff(self.list_)))
