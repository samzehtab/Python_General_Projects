# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S08 E04: Romeo_list

file_name = input("Enter file name: ")

fh = open(file = file_name)
romeo_list = list()

for line in fh:
    for word in line.split():
        # print(word)
        if word not in romeo_list:
            romeo_list.append(word)
print(sorted(romeo_list))