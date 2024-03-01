# 1st input: enter height in meters e.g: 1.65
height = input("what is your height in meters?" )
# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in kilograms" )
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
answer=(float(weight)/float(height)**2)
final_answer=int(answer)
print(final_answer)