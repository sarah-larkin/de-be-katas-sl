from src.counter_intelligence import counter_intelligence

# def test_returns_string(): 
#     assert counter_intelligence("") == ""

def test_shifted_by_one(): 
    assert counter_intelligence("Y") == "X"
    assert counter_intelligence("W") == "X"

def test_shifted_by_one_and_upper(): 
    assert counter_intelligence("y") == "X"
    assert counter_intelligence("w") == "X"

def test_multi_letter_string(): 
    assert counter_intelligence("BCDY") == "ABCX"

def test_spaces_and_punctuation_ignored():
    assert counter_intelligence("BCD Y") == "ABC X"
    assert counter_intelligence("NKRRU YCKKZNKGXZ D") == "HELLO SWEETHEART X"

def test_full_sentence(): 
    assert counter_intelligence('ANVNVKNA CX YRLT DY IDLLQRWR XW HXDA FJH QXVN OAXV FXAT, MJAURWP G') == 'REMEMBER TO PICK UP ZUCCHINI ON YOUR WAY HOME FROM WORK, DARLING X'
    
def test_multi_letter_string_returns_upper_case(): 
    assert counter_intelligence('ngbk g toik jge :) d') == 'HAVE A NICE DAY :) X'
