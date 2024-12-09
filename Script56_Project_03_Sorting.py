# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 03: Sorting

def decremental_bubble_sort(lst : list) -> list:
    '''
    decremental sort of the given list using bubble method.
    '''
    n = len(lst)
    ls = lst.copy()
    
    while n >= 2:
        for i in range(1, n):
            if ls[i-1] < ls[i]:
                t = ls[i]
                ls[i] = ls[i - 1]
                ls[i - 1] = t
            else: continue
            #print(ls)    Debugging
        n -= 1
    return ls


def find_largest(lst : list) -> int:
    '''
    Find and return the largest element index in a given list.
    '''
    
    largest_elem = lst[0]
    largest_index = 0
    n = len(lst)
    
    for i in range(1, n):
        if lst[i] > largest_elem:
            largest_elem = lst[i]
            largest_index = i
    return largest_index

    
def decremental_selection_sort(lst : list) -> list:
    '''
    decremental sort of the given list using selection method.
    '''
    ls = lst.copy()
    selsorls = []
    n = len(lst)
    
    for i in range(n):
        larind = find_largest(ls)
        selsorls.append(ls.pop(larind))
    return selsorls
    

def incremental_quick_sort(lst : list) -> list:
    '''
    decremental sort of the given list using quick method.
    '''
    n = len(lst)
    if n < 2: return lst
    pivot = lst[0]
    
    less = [elem for elem in lst[1:] if elem <= pivot]
    greater = [elem for elem in lst[1:] if elem > pivot]
    #print(less, greater)    Debugging
            
    qsorls = incremental_quick_sort(less) + [pivot] +\
        incremental_quick_sort(greater)
    return qsorls


### Driver Code ###

#Getting a list
inp = input('Enter integers of your list separated by space: \n')
inpl = inp.split()
ls = list(map(int, inpl))

#Sorting using bubble method
bubsorls = decremental_bubble_sort(ls)
print('\nThe main list: ', ls)
print('\nThe decremental bubble-sorted list: ', bubsorls)

#Finding the largest element index 
# =============================================================================
# largest = find_largest(ls)
# print(largest)
# =============================================================================

#Sorting using selection method
selsorls = decremental_selection_sort(ls)
print('\nThe decremental selection-sorted list: ', selsorls)

#Sorting using quick method
qsorls = incremental_quick_sort(ls)
print('\nThe incremental quick-sorted list: ', qsorls)

#Finding the 1st and the 2nd maximum element in a given list
print(f'\nThe 1st maximum element is {qsorls[-1]}')
print(f'The 2nd maximum element is {qsorls[-2]}')

#Finding the 1st and the 2nd minimum element in a given list
print(f'\nThe 1st minimum element is {qsorls[0]}')
print(f'The 2nd minimum element is {qsorls[1]}')