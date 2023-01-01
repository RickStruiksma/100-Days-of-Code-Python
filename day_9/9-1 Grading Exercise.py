# Day 9-1 Grading Exercise: Write a program that converts a dictionary
# of student scores to dictionary with student grades

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student, score in student_scores.items():
    if score > 90:
        student_grades.update({student: "Outstanding"})
    elif score > 80:
        student_grades.update({student: "Exceeds Expectations"})
    elif score > 70:
        student_grades.update({student: "Acceptable"})
    else:
        student_grades.update({student: "Fail"})

#print(student_grades.items())
