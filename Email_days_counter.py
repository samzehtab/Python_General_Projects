# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S09 E02: Email_days_counter

file_name = input("Enter file name: ")

fh = open(file = file_name)
daysdict = dict()

for line in fh:
    if line.startswith("From "):
        linelist = line.split()
        day = linelist[2]
        daysdict[day] = daysdict.get(day, 0) + 1
        
print(daysdict)