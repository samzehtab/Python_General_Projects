# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S09 E03: Email_counter

file_name = input("Enter file name: ")

fh = open(file = file_name)
email_counter_dict = dict()

for line in fh:
    if line.startswith("From "):
        line_list = line.split()
        email = line_list[1]
        email_counter_dict[email] = email_counter_dict.get(email, 0) + 1
        
print(email_counter_dict)