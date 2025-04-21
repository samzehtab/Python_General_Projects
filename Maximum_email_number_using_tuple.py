# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S10 E01: Maximum_email_number_using_tuple

file_name = input("Enter file name: ")

fh = open(file = file_name)
email_counter = dict()

for line in fh:
    if line.startswith("From "):
        line_list = line.split()
        email = line_list[1]
        email_counter[email] = email_counter.get(email, 0) + 1
        
# print(email_counter)    #Debugging

list_of_tuples = email_counter.items()
sorted_list = sorted(list_of_tuples, key=lambda x : x[1],
                     reverse=True)
print(f"{sorted_list[0][0]} {sorted_list[0][1]}")