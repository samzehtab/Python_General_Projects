#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S6 Book Exercises: Fruitfull Functions

import sys

def test(did_pass):
    '''
    Print the result of a test.
    '''

    linenum = sys._getframe(1).f_lineno

    if did_pass:
        msg = 'Test at line {0} OK.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)

    print(msg)


def test_suite():
    '''
    Run the suite of tests for code in this module.
    '''
    # Ex01
    test(turn_clockwise('N') == 'E')
    test(turn_clockwise('W') == 'N')
    test(turn_clockwise(42) == None)
    test(turn_clockwise('rubbish') == None)
    # Ex02
    test(day_name(3) == 'Wednesday')
    test(day_name(6) == 'Saturday')
    test(day_name(42) == None)
    # Ex03
    test(day_num('Friday') == 5)
    test(day_num('Sunday') == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num('Thursday')) == 'Thursday')
    test(day_num('Halloween') == None)
    # Ex04
    test(day_add('Monday', 4) == 'Friday')
    test(day_add('Tuesday', 0) == 'Tuesday')
    test(day_add('Tuesday', 14) == 'Tuesday')
    test(day_add('Sunday', 100) == 'Tuesday')
    # Ex05
    test(day_add('Sunday', -1) == 'Saturday')
    test(day_add('Sunday', -7) == 'Sunday')
    test(day_add('Tuesday', -100) == 'Sunday')


# Ex01
def turn_clockwise(direction: str) -> str:
    '''
    Showing the next direction by turning clockwise
    '''
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'
    else:
        return None


# Ex02
def day_name(day_number: int) -> str: 
    '''
    Enter day number from 0 to 6 and get
    day name from Sunday to Saturday
    '''

    if day_number == 0:
        return 'Sunday'
    elif day_number == 1:
        return 'Monday'
    elif day_number == 2:
        return 'Tuesday'
    elif day_number == 3:
        return 'Wednesday'
    elif day_number == 4:
        return 'Thursday'
    elif day_number == 5:
        return 'Friday'
    elif day_number == 6:
        return 'Saturday'
    else:
        return None


# Ex03
def day_num(day_namee: str) -> int: 
    '''
    Enter day name from Sunday to Saturday 
    and get day number from 0 to 6
    '''

    if day_namee == 'Sunday':
        return 0
    elif day_namee == 'Monday':
        return 1
    elif day_namee == 'Tuesday':
        return 2
    elif day_namee == 'Wednesday':
        return 3
    elif day_namee == 'Thursday':
        return 4
    elif day_namee == 'Friday':
        return 5
    elif day_namee == 'Saturday':
        return 6
    else:
        return None


# Ex04
def day_add(stday: str, delta: int) -> str:
    '''
    Adding days to a starting day
    and shows the final day
    '''
    adding = day_num(stday) + delta
    rem7 = adding % 7
    fiday = day_name(rem7)
    return fiday

### Driver Code ###

test_suite()
