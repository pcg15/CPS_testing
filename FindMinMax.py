def FindMinMax(list1):
"""
Returns the tuple of the minimum and maximum of a list of numbers.
:param list1: List of the numbers that are either int or float
:returns: The tuple of the minimum and maximum of the given list
:raises ImportError: error raised if logging module not found
:raises TypeError: error raised if input is not a list or a tuple
:raises ValueError: error raised if input has non-numerical values
"""
import logging
    logging.basicConfig(filename = 'FindMinMax.log', mt='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %pi')
    logging.info('Begin')
    try:
        import logging
	except ImportError:
        print("Cannot import logging")
		logging.debug('Make sure you have "logging" module.')
    try: 
        list1 = list(list1)
    except TypeError:
        print("Give a list please!")
		logging.error('You did not give an input of type "list" or "tuple".')
    for x in list1:
		try:
            x = float(x)
		except ValueError:
        print("Give a list with numbers!")
        logging.error('Your input has some non-numerical values.')
    try:
        print(list1[1])
    except:
        print("You need more than one number in the list!")      
        logging.warning('Give a list or else you will have two equal values in output tuple.')
    Minimum = min(list1)
    logging.info('Recorded the minimum value')
    Maximum = max(list1)
    logging.info('Recorded the maximum value')
    tup = (Minimum, Maximum)
    logging.info('Created the tuple')
    return tup
	logging.info('Finish')
