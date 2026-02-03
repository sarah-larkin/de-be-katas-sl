from src.parenthesis import find_closing_parenthesis

def test_returns_neg_one_if_not_valid():
    assert find_closing_parenthesis("", 0) == -1
    assert find_closing_parenthesis("") == -1
