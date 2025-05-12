# Mohammad Hossein Zehtab
# Advanced_Python_Wednesdays
# Project01: Python_Linear_Search_Function

def test(did_pass):
    """
    Print the result of a test.
    """
    if did_pass:
        print('True')
    else:
        print('Failed')


def search_linear(xs : list, target : str|int|float) -> int:
    """
    Searching sequence xs for target and returning its position (index),
    returning -1 if target does not exist in sequence xs. 

    Parameters
    ----------
    xs : list
        A sequence (e.g., a list) containing the items to be searched.
    target : str|int|float
        The item you are trying to find within the sequence.

    Returns
    -------
    int
        The index (position) of the target item within the sequence xs if found.

    """
    index = 0
    for item in xs:
        if str(item) == str(target):
            return index
        index += 1
    return -1


def test_suite():
    """
    Run the suite of tests for code in this module.
    """
    friends = ["Mohammad", "Ali", "Fatemeh", "Hassan", "Hossein", "Zeinab",
               "Kulthum"]
    test(search_linear(friends, "Ali") == 1)
    test(search_linear(friends, "Mohammad") == 0)
    test(search_linear(friends, "Kulthum") == 6)
    test(search_linear(friends, "Abbas") == -1)

### Driver Code ###
test_suite()