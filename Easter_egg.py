# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S07 E03: Easter_egg

file_name = input("Enter file name: ")

try:
    fh = open(file_name)
    count = 0
    
    for line in fh:
        if line.startswith("Subject"):
            count += 1
    print(f"There were {count} subject lines in {file_name}")
    
except:
    if file_name == "na na boo boo":
        print("NA NA BOO BOO TO YOU, You have been punk'd!")
    else:
        print("File can not be opened:", file_name)