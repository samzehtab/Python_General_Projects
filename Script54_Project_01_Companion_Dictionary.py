# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 01: Companion Dictionary

word_num = int(input('Number of words that exist in Dictionary: '))
word_list = list()
cdvalues = list()
compdict = dict()
count = -1

for _ in range(word_num):
    word_list = input('\nEnter your word and its three meanings\
                         in English, French and Germany respectively\
                         separated by space:\n')
    wl = word_list.split()
    compdict[wl[0]] = wl[1:]

cv = list(compdict.values())
for m in range(len(cv)):
    for n in range(len(cv[m])):
        cdvalues.append(cv[m][n])
# =============================================================================
# cdvalues.append(cv[m, n] for m in range(len(cv))\
#                 for n in range(len(cv[m])))
# =============================================================================

sentence = input('\nEnter the sentence you want to translate:\n')
sl = sentence.split()

for s in sl:
    count += 1
    if s in cdvalues:
        for i in compdict:
            if s in compdict[i]:
                key = i
# =============================================================================
#         key = [i for i in compdict if s in compdict[i]]
# =============================================================================
        sl[count] = str(key)
        #print(sl)    Debugging
    else: continue

print('\n\nThe translated sentence is:\n', ' '.join(sl))