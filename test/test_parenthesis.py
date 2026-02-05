from src.parenthesis import find_closing_parenthesis

def test_returns_neg_one_if_not_valid():
    assert find_closing_parenthesis("", 0) == -1
#     assert find_closing_parenthesis("") == -1

# def test_returns_neg_one_with_no_parenthesis(): 
#     assert find_closing_parenthesis("hello") == -1

def test_returns_index_with_one_set_of_parenthesis():
    assert find_closing_parenthesis("(hello)", 1) == 6

def test_returns_index_when_two_sets_of_parenthesis():
    assert find_closing_parenthesis("Hello, (world). (Something Else).", 2) == 31

def test_returns_index_when_multiple_sets_of_parenthesis():
    assert find_closing_parenthesis("Hello, (world, (foo) bar (something) else), foo (bar) cat", 3) == 35

def test_returns_index_with_nested_parenthesis(): 
    assert find_closing_parenthesis("Hello, (world, (foo) bar (something) else), foo (bar) cat", 1) == 41