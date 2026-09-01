Student_marks=[90,76,80,50]
print(len(Student_marks))
total_marks=0
for i in Student_marks:
    total_marks+=i
print("Total marks are",total_marks)
avg=total_marks/len(Student_marks)
print("Average:",avg)
Student_marks.sort()
print("The lowest marks achieved by the student is:",Student_marks[0])
print("The most marks achieved by the student is:",Student_marks[-1])
