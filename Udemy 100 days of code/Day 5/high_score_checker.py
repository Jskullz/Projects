# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
score=0
not_high_score=0
for highscore in student_scores:
  if highscore>=score:
    score=highscore
  else:
    highscore=not_high_score
print(f"The highest score in the class is: {score}")