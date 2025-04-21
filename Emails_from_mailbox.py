# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S08 E05: Emails_from_mailbox

file_name = input("Enter file name: ")

fh = open(file = file_name)
count = 0

for line in fh:
    if line.startswith("From:"):
        fromline = line.split()
        print(fromline[1])
        count += 1
print(f"There were {count} lines in the file with From as the first word")