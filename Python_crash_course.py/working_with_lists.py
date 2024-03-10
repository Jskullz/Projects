#numbers range from 1 to 100
numbers=list(range(1,101))
print(numbers)
#prints the lowest number in the list
print(min(numbers))
#prints the highest number in the list
print(max(numbers))
#adds all the numbers in the list
print(sum(numbers))
#displays the first 25 numbers in the list
print(numbers[0:25])

#displays all numbers in list by 2
print(numbers[1:101:2])

#displays odd numbers in the list
print(numbers[0:101:2])

squares=[]
for value in range(1,100):
    square=value**2
    squares.append(square)
print(squares)