# Day 5-1 Average Heights: Write a script that calculates the average of
# a list of student heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

count = 0
total_height = 0
for height in student_heights:
    count += 1
    total_height += height
average_height = total_height / count
print(average_height)
