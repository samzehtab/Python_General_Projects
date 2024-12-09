# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# S20 Book Ex02: Add Fruit

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
    
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)
    
    add_fruit(new_inventory, "strawberries", 25)
    #print(new_inventory)    Debugging
    test(new_inventory["strawberries"] == 35)
    
    
def add_fruit(inventory : dict, fruit : str, quantity=0):
    '''
    Adding Fruit to a Dictionary
    '''
    
    if fruit in inventory:
        inventory[fruit] += quantity
        return inventory
    
    inventory[fruit] = quantity
    return inventory


### Driver Code ###
test_suite()