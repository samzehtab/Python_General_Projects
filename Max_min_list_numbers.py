# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S08 E06: Max_min_list_numbers

num_list = list()

while True:
    num = input("Enter a number: ")
    
    if num == "done": break

    num_list.append(int(num))
    
print("Maximum", max(num_list))
print("Minimum", min(num_list))