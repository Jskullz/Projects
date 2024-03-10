car_brands = ['toyota', 'honda', 'bmw', 'audi']
print("\n Printing the list of car brands")
print(car_brands)
print("\n Printing the first element of the list")
print(car_brands[0])
car_brands[0] = 'ford'
print("\n Changing the first element of the list to 'ford'")
print(car_brands)
car_brands.append('toyota')
print("\n Appending 'toyota' to the list")
print(car_brands)

car_brands.insert(0, 'toyota')
print("\n Inserting 'toyota' at the beginning of the list")
print(car_brands)

del car_brands[-1]
print("\n Deleting the last element of the list")
print(car_brands)

#In programming, .pop() typically refers to a method or function used to remove 
#and return an element from a data structure, often an array, list, or stack. 
#The element that is removed is usually specified by its index within the data structure.
popped_car_brand = car_brands.pop()
print("\n Popping the last element of the list")
print(popped_car_brand)
print(car_brands)

sorted_car_brands = sorted(car_brands)
print("\n Sorting the list")
print(sorted_car_brands)

car_brands.sort()
print("\n Sorting the list")
print(car_brands)

car_brands.sort(reverse=True)
print("\n Sorting the list in reverse order")
print(car_brands)

car_brands.reverse()
print("\n Reversing the list")
car_brands.insert(0,"audi")
print("\n Inserting 'audi' at the beginning of the list")
print(car_brands)

print("\n Finding the length of the list")
print(len(car_brands))