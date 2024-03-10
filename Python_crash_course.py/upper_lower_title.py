name="julie"
print(name.title())

list_of_names=["julie","john","james","jane"]
for name in list_of_names:
    print(name.title())

for name in list_of_names:
    print(name.upper())

for name in list_of_names:
    print(name.lower())

sorted_names=sorted(list_of_names)

for name in sorted_names:
    print(f"your name is {name.title()}, your name in upper case is {name.upper()} and your name in lower case is {name.lower()}")