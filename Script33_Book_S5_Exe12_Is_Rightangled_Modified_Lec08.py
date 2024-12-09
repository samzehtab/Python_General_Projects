
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S5 Book Exc12: Is Rightangled Function Modified

def is_rightangled_2(side1: float, side2: float, side3: float) -> bool:
    '''
    Is This Triangle Rightangled?
    '''
    
    if (side3 > side1) and (side3 > side2):
        addsq = side1 ** 2 + side2 ** 2
        if abs(addsq - side3 ** 2) < 0.000001:
            return 'True'
        return 'False'

    elif (side2 > side1) and (side2 > side3):
        addsq = side1 ** 2 + side3 ** 2
        if abs(addsq - side2 ** 2) < 0.000001:
            return 'True'
        return 'False'
    
    else:
        addsq = side2 ** 2 + side3 ** 2
        if abs(addsq - side1 ** 2) < 0.000001:
            return 'True'
        return 'False'
