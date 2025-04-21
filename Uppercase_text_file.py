# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S07 E01: Uppercase_text_file

file_name = input("Enter a file name: ")
print()

fh = open(file=file_name)

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line, sep="")