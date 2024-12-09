# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Bonus Project S20 Ex03 & 04: Alice Words

# Exercise 03
textlist = list()
word_dict = dict()

filer = 'Alice\'s Adventures in Wonderland.txt'
fhr = open(filer, mode = 'r')
text = fhr.read()

# Considering alphabetical letters 
# Turning uppercase into lowercase
# Spliting the text into words in a list
for letter in text:
    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122\
        or ord(letter) == 39 or ord(letter) == 32\
            or ord(letter) == 10 or ord(letter) == 45:
        if letter.isupper():
            letter = letter.lower()
        textlist.append(letter)
    else: continue
lowertext = ''.join(textlist)
#print(lowertext)    debugging
lowertextlist = lowertext.split()

# Counting words of the list
for word in lowertextlist:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# Arranging table of word and counts
wordcounter_dict_items = list(word_dict.items())
wordcounter_list = list(map(list, wordcounter_dict_items))
wordcounter_list.sort()

# Writing table of word and counts into a text file
filew = 'alphabetical-ordered word counter list.txt'
fhw = open(filew, 'w')
fhw.write('Word\t\t   Count\n')
fhw.write('=' * 25)
for item in wordcounter_list:
    wordlen = len(item[0])
    space = 20 - wordlen
    fhw.write(f'\n{item[0]}' + ' ' * space + f'{item[1]}')

# Showing the occurance of the word 'alice' in the book
print(f'\nthe word "alice" occurs in the book '
      f'{word_dict["alice"]} times.')

fhr.close()
fhw.close()

# Exercise 04
# Finding and showing the longest word in the book
word_dict_keys_list = list(word_dict.keys())
maxword = max(word_dict_keys_list, key = len)
print(f'\n{maxword} is the longest word in '
      f'the book and has {len(maxword)} characters.')