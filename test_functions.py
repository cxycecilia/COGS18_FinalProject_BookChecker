"""Test for my functions."""

from functions import check_numbr, check_price

def test_check_number():
    """Test for the function check_number."""
    
    assert check_number(2654) == 'The book is on the right side on the first floor.'
    assert check_number(6834) == 'Sorry, the book is now out of stock.'
    assert check_number(137.2) == 'Sorry, please enter the right number.'
    
def test_check_price():
    """Test for the function check_price."""
    
    assert check_price(22.42, 18.66, 37.99) == 79.07
    assert check_price(22.42, 18.66, 37.99, 103.56) == 164.367