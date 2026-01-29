from src.sum_duplicates import sum_consecutive_duplicates, reduce_consecutives

def test_no_duplicate(): 
    assert sum_consecutive_duplicates([1, 2, 3]) == [1, 2, 3]

def test_one_duplicate(): 
    assert sum_consecutive_duplicates([1, 1, 2, 3]) == [2, 2, 3]

def test_multiple_duplicates(): 
    assert sum_consecutive_duplicates([1, 1, 2, 2, 3, 3]) == [2, 4, 6]

def test_more_multiple_duplicates(): 
    assert sum_consecutive_duplicates([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [2, 2, 4, 2, 3]


def test_reduce_consecutives(): 
    assert reduce_consecutives([1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1]) == [8, 2, 3]