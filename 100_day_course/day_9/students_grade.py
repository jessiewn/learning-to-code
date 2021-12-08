student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
students_grade={}
for score in student_scores:
    if student_scores[score] > 90 and student_scores[score]<100:
        student_scores[score] = 'Outstanding'
    elif student_scores[score] > 81 and student_scores[score] <90:
        student_scores[score] = 'Exceeds Expectations'
    elif student_scores[score] > 71 and student_scores[score] <80:
        student_scores[score] = 'Acceptable'
    else:
        student_scores[score] = 'Fail'
students_grade = student_scores
print(students_grade)
    
    