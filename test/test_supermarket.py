from src.supermarket import queue_time

def test_queue_time_returns_0_if_no_customers():
    assert queue_time([], 1) == 0
    assert queue_time([], 5) == 0

def test_queue_time_returns_error_if_no_checkouts(): 
    assert queue_time([1], 0) == "error"
    assert queue_time([5, 2, 3], 0) == "error"

def test_queue_time_returns_int(): 
    assert queue_time([1], 1) == 1
    result = queue_time([1], 1)
    assert isinstance(result, int)

def test_queue_time_returns_sum_of_list_when_one_checkout(): 
    assert queue_time([2, 2, 2], 1) == 6
    assert queue_time([2, 4, 6], 1) == 12

def test_queue_time_returns_highest_no_when_2_customers_and_2_checkouts(): 
    assert queue_time([2, 10], 2) == 10
    assert queue_time([1, 15], 2) == 15
    assert queue_time([20, 3], 2) == 20

def test_queue_time_returns_sum_of_half_queue_when_2_checkouts(): 
    assert queue_time([2, 2, 2], 2) == 4
    assert queue_time([2, 3, 10], 2) == 12