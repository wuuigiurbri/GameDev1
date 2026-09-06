import random
from faker import Faker

fake = Faker()

student_marks = []
for i in range(20):
    random_name= fake.first_name()
    random_mark= random.randint(0, 100)
    student_marks.append([random_mark,random_name])

least = [] # <= 30
medium = [] # 31 to 69
most = [] # >= 70


for i in range(len(student_marks)):
    student = student_marks[i]
    mark = student[0]
    
    if mark <= 30:
        least.append(student)
        
    if mark >= 31 and mark <= 69:
        medium.append(student)
        
    if mark >= 70:
        most.append(student)

least.sort()
medium.sort()
most.sort()

print("\n Low Scores")
for i in range(len(least)):
    print(least[i][0], least[i][1])

print("\n Average Scores")
for i in range(len(medium)):
    print(medium[i][0], medium[i][1])

print("\n High Scores")
for i in range(len(most)):
    print(most[i][0], most[i][1])
