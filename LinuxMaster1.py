marks = [90, 25, 67, 45, 80]

#for i, mark in enumerate(marks):

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d 번 학생: 합격" % number)
    else:
        print("%d 번 학생: 불합격" %number)
