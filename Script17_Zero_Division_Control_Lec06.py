#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#Zero Division Control

x = int(input('x = '))
y = int(input('y = '))

try:
    print(f'{x/y}        {x//y}        {x%y}')
except:
    print('zero division occured.')
