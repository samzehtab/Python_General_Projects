# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 05: File Processing

textlist = list()
letter_frequency_dict = dict()

file = 'The Wonderful Wizard of Oz by L. Frank Baum.txt'
fh = open(file, mode = 'r')
text = fh.read()

for l in text:  # Separating each letter of the text and putting it in a list
    textlist.append(l)

for letter in textlist:
    
    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:  #We only want a-z letters
        
        if letter.isupper():  # Turning uppercase into lowercase
            letter = letter.lower()
            
        if letter not in letter_frequency_dict:  # Counting letter frequency using dictionary
            letter_frequency_dict[letter] = 1
        else:
            letter_frequency_dict[letter] += 1
            
    else: continue  # Ignoring everything except a-z letters

dictitems = list(letter_frequency_dict.items())  # Converting dictionary to list
letter_frequency_list = list(map(list, dictitems))

for item in letter_frequency_list:  # Swapping letter and frequency for sorting
    item[0], item[1] = item[1], item[0]
    
letter_frequency_list.sort(reverse=True)  # Decremental sorting

print(f'Letter Frequency in {file}\n')  # Making table
print('Letter\t\tFrequency')
print('=' * 30)
for pair in letter_frequency_list:
    print(f'  {pair[1]}\t\t\t   {pair[0]}')

fh.close()