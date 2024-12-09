
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S5 Exc06 Book: Exam Grade

def exam_grade(mark: float) -> str:
    '''
    Exam mark to exam grade
    '''
    
    if mark >= 75: return 'First'
    elif 70 <= mark <75: return 'Upper Second'
    elif 60 <= mark <70: return 'Second'
    elif 50 <= mark <60: return 'Third'
    elif 45 <= mark <50: return 'F1 Supp'
    elif 40 <= mark <45: return 'F2'
    else: return 'F3'
### Driver Code ###

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
for m in xs:
    xsgrade = exam_grade(m)
    print(f'The Grade of {m}    is Equal to {xsgrade}')
