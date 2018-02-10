import numpy as np


def test_positive_numbers():
    from FindMinMax import FindMinMax
    list1 = list(range(1, 11))
    assert FindMinMax(list1) == (1, 10)


def test_negative_numbers():
	from FindMinMax import FindMinMax
	list2 = list(range(-12, -1))
	assert FindMinMax(list2) == (-12, -2)


def test_floats():
	from FindMinMax import FindMinMax
	list3 = np.arange(-1.0, 1.1, 0.1)
	tup = FindMinMax(list3)
	assert abs(tup[0] +1.0) < 0.00001
	assert abs(tup[1] - 1.0) < 0.00001


def test_fractions():
	from FindMinMax import FindMinMax
	list4 = np.arange(1/3, 5/3, 1/3)
	tup = FindMinMax(list4)
	assert abs(tup[0]-1/3) < 0.00001
	assert abs(tup[1]-5/3) < 0.00001

