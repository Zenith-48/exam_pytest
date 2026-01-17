from leap_year import leap
def test_leap_year():
    assert leap("2028")==True
def test_not_leap_year():
    assert leap("1900")==False
def test_leap_not_a_year():
    assert leap("2000")==True
