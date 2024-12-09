
# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec 12: List Multiplication Function

def test(did_pass):
    '''
    Print the result of a test.
    '''
     
    if did_pass:
        print('True')
    else:
        print('Failed')


def mymul(xs: list) -> float:
    '''
    Multiply all the numbers in the list xs,
    and return the product.
    '''
    prod = 1
    for x in xs:
        prod *= x
    return prod


def test_suite():
    '''
    Run the suite of tests for code in this module.
    '''
    test(mymul([1, 2, 3]) == 6.0)
    test(mymul([0, 3, 4]) == 0.0)
    test(mymul([-1, -1, 5]) == 5.0)

### Driver Code ###
test_suite()
