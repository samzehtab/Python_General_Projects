# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S09 E05: Domain_counter

file_name = input("Enter file name: ")

fh = open(file = file_name)
domain_counter_dict = dict()

for line in fh:
    if line.startswith("From "):
        line_list = line.split()
        
        email = line_list[1]
        domain_start_index = email.find("@") + 1
        domain = email[domain_start_index:]
        domain_counter_dict[domain] = domain_counter_dict.get(domain, 0) + 1
        
print(domain_counter_dict)