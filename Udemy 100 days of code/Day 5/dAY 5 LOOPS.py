# fruits=["apple","pear","banana","orange","grapes"]
# for fruit in fruits:
#     if fruit!="banana":
#         print(fruit + " is not a banana")
#     else:
#         print(fruit + " is a banana")

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total=0
number_of_students=0
for average in student_heights:
  total+=average
  number_of_students+=1
  

final=round(total/number_of_students)
print(f"total height = {total}")
print(f"number of students = {number_of_students}")
print(f"average height = {final}")