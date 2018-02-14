def summation(list_):
    import numpy as np
    sum_list_ = np.sum(list_)
    return sum_list_
    try:
        import numpy
    except ImportError:
        raise ImportError('Virtual environment not activated. Cannot import numpy.')
