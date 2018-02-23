def test_Assignment06():
    from assignment06 import Assignment06
    list_ = [1, 5, -6, 7.25]
    function = Assignment06(list_)
    assert function.Sum == 7.25
    assert (function.Sum-7.25) < .00001
    assert function.MinMax == (-6, 7.25)
    assert function.MaxDiff == 13.25


def test_excepts():
    import pytest
    import math
    with pytest.raises(ImportError, message="Anticipated ImportError"):
        import anypackage
    with pytest.raises(TypeError, message="Anticipated TypeError"):
        int_list = 1 + [1, 2, 4]
        int_str = 3 + "hello"
        list_str = [1, 2, 4] + "hello"
    with pytest.raises(ValueError, message="Anticipated ValueError"):
        val = int("hello")
