# def greet():
#     print("Hello")
#     print("Good Morning")
#     print("Good Afternoon")
# greet()
# name= input("Enter your name: ")
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#     print(f"Isn't the weather lovely today {name}")
# greet_with_name(name)
name = input("What is your name: ")
location = input("Where are you from: ")
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with(location=location,name=name)
