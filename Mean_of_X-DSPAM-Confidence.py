# In the name of God
# Mohammad Hossein Zehtab
# Advanced-Python-Wednesdays
# Py4e S07 E02: Mean_of_X-DSPAM-Confidence

file_name = input("Enter file name: ")

fh = open(file_name)
summation = 0
count = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence"):
        code = line[-7:]
        # print(code)    # Debugging
        summation += float(code)
        count += 1
average = summation / count
print("Average spam confidence: ", average)