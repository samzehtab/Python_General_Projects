# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S10 E02: Emails_hour_numbers

file_name = input("Enter file name: ")

fh = open(file = file_name)
email_hour_number = dict()

for line in fh:
    if line.startswith("From "):
        line_list = line.split()
        email_time = line_list[5]
        time_list = email_time.split(sep=":")
        hour = time_list[0]
        
        email_hour_number[hour] = email_hour_number.get(hour, 0) + 1

for key, value in sorted(email_hour_number.items()):
    print(f"{key} {value}")