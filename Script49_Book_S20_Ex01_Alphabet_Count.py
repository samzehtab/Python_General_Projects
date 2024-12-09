# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# S20 Book Ex01: Alphabet Count

st = input('Enter the string that you want to count its letters: ')
stlow = st.lower()
stlowns = ''.join(stlow.split())

count_letter = dict()
for letter in stlowns:
    count_letter[letter] = count_letter.get(letter, 0) + 1
    
count_letter_list = list(count_letter.items())
count_letter_list.sort()
result = dict(count_letter_list)

for keys, values in result.items():
    print(f'{keys}\t{values}')