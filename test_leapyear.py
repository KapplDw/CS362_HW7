import leapyear


def test_leaps():
    assert leapyear.leap(2020) == True
    assert leapyear.leap(2000) == True



def test_nleaps():
    assert leapyear.leap(2021) == False
    assert leapyear.leap(2001) == False