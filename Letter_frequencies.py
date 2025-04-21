# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S10 E03: Letter_frequencies

import string

file_name = input("Enter file name: ")

fh = open(file = file_name)
char_counter_dict = dict()

for line in fh:
    line = line.rstrip()
    line = line.lower()
    # print(line)    #Debugging
    
    line = line.translate(str.maketrans("", "", string.punctuation))
    # print(line)    #Debugging
    
    line = line.translate(str.maketrans("", "", "1234567890 \t"))
    # print(line)    #Debugging
    
    for char in line:
        char_counter_dict[char] = char_counter_dict.get(char, 0) + 1
        
letter_frequencies = sorted(char_counter_dict.items(), 
                            key=lambda x:x[1],
                            reverse=True)

number_of_chars = sum(char_counter_dict.values())

for item in letter_frequencies:
    freq = round(item[1] * 100 / number_of_chars, 1)
    print(f"{item[0]} {freq}%")