# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec21:Ternary Search

def ternary_search(xs, target):
    '''
    Search for index of the target in the sorted list of xs
    Using Ternary Search System
    '''
    left = 0
    right = len(xs) - 1
    
    while left <= right:
        
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
    return -1

### Driver Code ###

xs = [12, 20, 28, 33, 41, 58, 62, 85, 90]
target = 41

r = ternary_search(xs, target)
print(r)