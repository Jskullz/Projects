line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


letter_to_index={"A":0,"B":1,"C":2}
number_to_index={"1":0,"2":1,"3":2}
row=position[0]
collum=position[1]
row_index=letter_to_index[row]
collum_to_index=number_to_index[collum]

map[collum_to_index][row_index]="X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")