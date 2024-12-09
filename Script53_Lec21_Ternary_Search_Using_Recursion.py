# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec21: Ternary Search Using Recursion

def recursion_ternary_search(xs, target, left = 0, right = 'test'):
    '''
    Search for index of the target in the sorted list of xs
    Using Recursion Type of Ternary Search System
    '''
    if right == 'test':
        right = len(xs) - 1
        
    if right < left: 
        return -1
    else:
        third1 = left + (right - left) // 3
        third2 = right - (right - left) // 3
        third1item = xs[third1]
        third2item = xs[third2]
        
        if target == third1item:
            return third1
        elif target == third2item:
            return third2
        elif target < third1item:
            right = third1 - 1
        elif target > third2item:
            left = third2 + 1
        else:
            left = third1 + 1
            right = third2 - 1
        
        return recursion_ternary_search(xs, target, left, right)

### Driver Code ###

xs = [12, 20, 28, 33, 41, 58, 62, 85, 90]
target = 85

r = recursion_ternary_search(xs, target)
print(r)