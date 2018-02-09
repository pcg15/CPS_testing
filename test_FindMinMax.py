def test_positive_numbers():
    from FindMinMax import FindMinMax
    list1 = list(range(1,11))
    print(list1)
    assert FindMinMax(list1) == (1,10)
