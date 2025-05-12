# Mohammad Hossein Zehtab
# Advanced_Python_Wednesdays
# Project02: Python_Binary_Search_Function

def test(did_pass):
    """
    Print the result of a test.
    """
    if did_pass:
        print('True')
    else:
        print('Failed')


def search_binary(xs, target):
    """
    Find and return the index of target in sequence xs using a faster method
    called binary search.
    """
    
    lb = 0
    ub = len(xs)
    
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1
    
        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2
    
        # Fetch the item at that position
        item_at_mid = xs[mid_index]
    
        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))
    
        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
            
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
            
        else:
            ub = mid_index        # Use lower half of ROI next time


def test_suite():
    """
    Run the suite of tests for code in this module.
    """
    xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(search_binary(xs, v) == i)

### Driver Code ###
test_suite()