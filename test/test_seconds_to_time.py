from src.seconds_to_time import seconds_to_time

def test_one_second(): 
    assert seconds_to_time(1) == "1 second"

def test_plural_seconds(): 
    assert seconds_to_time(2) == "2 seconds"

def test_one_minute(): 
    assert seconds_to_time(60) == "1 minute"

def test_two_minues(): 
    assert seconds_to_time(120) == "2 minutes"

def test_mins_and_seconds(): 
    assert seconds_to_time(121) == "2 minutes and 1 second"

def test_hour(): 
    assert seconds_to_time(3600) == "1 hour"

def test_hours(): 
    assert seconds_to_time(7200) == "2 hours" 

def test_hour_min_sec(): 
    assert seconds_to_time(3661) == "1 hour, 1 minute and 1 second"

def test_hours_mins_secs(): 
    assert seconds_to_time(7322) == "2 hours, 2 minutes and 2 seconds"
