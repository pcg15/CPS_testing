def test_Assignment06():
    from assignment06 import Assignment06
    list_ = [1, 5, -6, 7.25]
    function = Assignment06(list_)
    assert function.Sum == 7.25
    assert (function.Sum-7.25) < .00001
    assert function.MinMax == (-6, 7.25)
    assert function.MaxDiff == 13.25
