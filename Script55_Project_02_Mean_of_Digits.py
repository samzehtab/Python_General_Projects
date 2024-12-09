# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 02: Mean of Digits

def test(ls : bool):
    '''
    Test if the sentence of ls is True.
    '''
    if ls:
        print ('OK')
    else:
        print('FAILED')

def test_suite():
    '''
    Perform some tests.
    '''
    test(find_mean_of_digits_in(1326) == 3.0)
    test(find_mean_of_digits_in(-56789) == 7.0)
    

def find_mean_of_digits_in(number : int) -> float:
    '''
    find and return the average of digits of the number.
    '''
    
    count = 0
    summ = 0
    num = abs(number)
    
    while num > 0:
        summ += num % 10
        num = num // 10
        count += 1
    ave = summ / count
    return ave

### Driver Code ###
test_suite()