# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec21: Binary Search Using Recursion

def recursion_binary_search(xs, target, left = 0, right = 'test'):
    '''
    Search for index of the target in sorted list of xs.
    '''
    if right == 'test':
        right = len(xs) - 1
    
    if right < left: 
        return -1
    else:
        mid = (left + right) // 2
        mid_item = xs[mid]
        
        if mid_item == target:
            return mid
        elif mid_item > target:
            right = mid - 1
        else:
            left = mid + 1
            
        return recursion_binary_search(xs, target, left, right)

### Driver Code ###

xs = [5, 12, 28, 35, 40, 45]
target = 28

r = recursion_binary_search(xs, target)
print(r)