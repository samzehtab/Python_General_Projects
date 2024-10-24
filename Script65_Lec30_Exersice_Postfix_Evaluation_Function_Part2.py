# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec30 Exercise: Postfix Evaluation Function Part 2

import re

class Stack:
    '''
    Creates a new stack.
    '''
    
    def __init__(self):
        '''
        Creates a new stack using python list class.
        '''
        self.items = []
        
    def push(self, item):
        '''
        Append a new item in the stack.
        '''
        self.items.append(item)
        
    def pop(self):
        '''
        Pop and return the last item on the top of the stack.
        '''
        return self.items.pop()
    
    def is_empty(self):
        '''
        Check that stack is empty or not.
        '''
        return (self.items == [])
    
    def __str__(self):
        return f'{self.items}'
    
def  eval_postfix(exp):
    '''
    Evaluates a postfix expresion
    '''
    token_list = re.split('', exp)
    
    stack = Stack()
    
    for token in token_list:
        if token == '' or token == ' ': continue
    
        elif token == '+':
            summ = stack.pop() + stack.pop()
            stack.push(summ)
            
        elif token == '*':
            prod = stack.pop() * stack.pop()
            stack.push(prod)
            
        elif token == '/':
            denominator = stack.pop()
            numerator = stack.pop()
            div = numerator / denominator
            stack.push(div)
            
        elif token == '-':
            subtrahend = stack.pop()
            minuhend = stack.pop()
            sub = minuhend - subtrahend
            stack.push(sub)
        
        else:
            stack.push(int(token))
        # print(stack)    Debugging
            
    return stack.pop()

### Driver Code ###
print(eval_postfix("5647+2*"))
print(eval_postfix("12+3 *"))
print(eval_postfix("263/4-*"))