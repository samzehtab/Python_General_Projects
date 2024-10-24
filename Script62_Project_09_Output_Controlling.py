# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 09: Output Controlling

try:
    for i in range(3):
        try:
            1 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError('Error: You divided by zero!')
        finally:
            print('Finally executed')

except ZeroDivisionError:
    print('Outer ZeroDivisionError exception caught')