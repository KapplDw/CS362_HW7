# Test fizzbuzz.py

import fizzbuzz

def multiple_three():
    assert fizzbuzz.fizzbuzz(3) == "Fizz"
    assert fizzbuzz.fizzbuzz(6) == "Fizz"

def multiple_five():
    assert fizzbuzz.fizzbuzz(5) == "Buzz"
    assert fizzbuzz.fizzbuzz(20) == "Buzz"