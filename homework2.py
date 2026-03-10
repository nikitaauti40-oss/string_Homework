
# you have one list of student marks 
# create two sublist for even and odd marks students

stu_marks = [20,40,60,90,70,50,35,33,87]
even_marks = []
odd_marks = []
for i in stu_marks:
    if i % 2 == 0:
        even_marks.append(i)
    else:
        odd_marks.append(i)
print("even:" ,even_marks)
print("odd:" ,odd_marks)


# output:
# even: [20, 40, 60, 90, 70, 50]
# odd: [35, 33, 87]
