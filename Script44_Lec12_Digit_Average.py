# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec 12: Mean of Digits Function

import math

def test(did_pass: bool):
    '''
    Print the result of a test.
    '''
     
    if did_pass:
        print('True')
    else:
        print('Failed')


def test_suite():
    '''
    Run the suite of tests for code in this module.
    '''
    test(find_mean_of_digits_in(1326) == 3.0)
    test(find_mean_of_digits_in(56789) == 7.0)


def find_mean_of_digits_in(number:int) -> float:
    '''
    Returns digits of a number in a list and
    Returns the mean of digits
    '''
    dig = ''
    count = 0
    
    while True:
        d = number % 10
        dig += str(d)
        number //= 10
        count += 1
        if number == 0:
            break
        
    digits = dig[::-1]
    print(list(map(int, digits)))
    
    return sum(list(map(int, digits))) / count

### Driver Code ###

test_suite()
