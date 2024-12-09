```python
# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# S11 Book Ex05-08: Vectors

def test(did_pass):
    '''
        Test if the statement is passed or not
    '''
    
    if did_pass:
        print('OK')
    else:
        print('Failed')


def test_suite():
    '''
        Evaluates a group of tests
    '''
    
    # Ex05
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    print()
    
    # # Ex06
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    print()
    
    # # Ex07
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    print()
    
    # Ex08
    test(cross_product([2, 3, 4], [5, 6, 7]) == [-3, 6, -3])
    test(cross_product([1, 1, 1], [2, 2, 2]) == [0, 0, 0])
    

#Ex05
def add_vectors(u, v):
    '''
        Corresponding summation of two vectors of the same length
    '''
    add = [0] * len(u)
    
    for i in range(len(u)):
        add[i] = u[i] + v[i]
        # print(f'add[{i}] =', add[i])     Debugging
    return add


#Ex06
def scalar_mult(s, v):
    '''
        Scalar multiple of vector by a scalar
    '''
    smult = list()
    
    for i in range(len(v)):
        smult.append(s * v[i])
    return smult


#Ex07
def dot_product(u, v):
    '''
        Summation of the products of the corresponding elements of two vectors of the same length
    '''
    dprod = 0
    
    for i in range(len(u)):
        prod = u[i] * v[i]
        dprod += prod
    return dprod


#Ex08
def cross_product(u, v):
    '''
        Cross product of two vectors of length 3
    '''
    cprod = [0] * 3
    
    cprod[0] = u[1] * v[2] - u[2] * v[1]
    cprod[1] = u[2] * v[0] - u[0] * v[2]
    cprod[2] = u[0] * v[1] - u[1] * v[0]
    
    return cprod


### Driver Code ###

test_suite()
```