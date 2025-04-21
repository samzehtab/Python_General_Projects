# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S09 E04: Maximum_email_number

file_name = input("Enter file name: ")

fh = open(file = file_name)
email_counter_dict = dict()

for line in fh:
    if line.startswith("From "):
        line_list = line.split()
        email = line_list[1]
        email_counter_dict[email] = email_counter_dict.get(email, 0) + 1
        

max_email_number = max(email_counter_dict.items(), key=lambda x : x[1])
print(f"{max_email_number[0]} {max_email_number[1]}")

# sorted_list = sorted(email_counter_dict.items(),
#                       key=lambda x : x[1], reverse=True)
# print(f"{sorted_list[0][0]} {sorted_list[0][1]}")