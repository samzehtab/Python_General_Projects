# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# S11 Book Ex10: Replace

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
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    
    test(replace(s, "om", "am") ==
          "I love spam! Spam is my favorite food. Spam, spam, yum!")
    
    test(replace(s, "o", "a") ==
          "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
    

def replace(s, old, new):
    '''
        Replaces all occurrences of old with new in a string s
    '''
    
    ls = list(s)
    
    for l in ls:
        if len(old) == 1:
            if l == old:
                ls[ls.index(l)] = new
            else: continue
        else:
            for j in range(len(old)):
                if ls[ls.index(l) + j] == old[j]:
                    ls[ls.index(l) + j] = new[j]
                else: continue
    return ''.join(ls)


### Driver Code ###

test_suite()
