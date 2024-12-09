# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Lec 12: List Including Negative Integers

numbers = [2, 6, -2, -80, 7, 19, 302, 1001,\
           6430, -2341, 3, -7]

numbers2 = [4, -3, 88, -9, -123, 14, 9999]

# Divisibility by 7

count = 0

for x in numbers2:
    if abs(x) % 7 != 0:
        continue
    else:
        count += 1
        
print('\nNumber of integers divisible by 7 is:', count)


# Summation of the evens

summation = 0

for x in numbers2:
    if abs(x) % 2 != 0:
        continue
    else:
        summation += x
        
print('\nSummation of the evens is:', summation)


# Multiplication of the negatives

prod = 1

for x in numbers2:
    if x>=0:
        continue
    else:
        prod *= x

print('\nMultiplication of the negatives is:', prod)


# Integers with 4 digits

c = 0

for x in numbers2:
    if 1000 <= abs(x) <10000:
        c += 1
    else:
        continue

print('\nNumber of integers with 4 digits is:', c)
