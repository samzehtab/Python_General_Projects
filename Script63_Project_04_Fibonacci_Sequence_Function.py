# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 04: Fibonacci Sequence Function

valuedict = {0: 0, 1: 1}

def fibonacci(index):
    '''
    Finding value of the index sentence of fibonacci sequence using recursive
    The series:  0   1   1   2   3   5   8   13  21  34  55  89  ...
    Indices:     0   1   2   3   4   5   6   7   8   9   10  11  ... 
    '''
    
    if index not in valuedict:
        new_sentence = fibonacci(index - 1) + fibonacci(index - 2)
        valuedict[index] = new_sentence
        
    return valuedict[index]

### Driver Code ###

index = 2000
result = fibonacci(index)
print(f'The {index}th sentence of fibonacci sequence is\n{result}')