# def format_name():
#     f_name = input("What is your first name? ")
#     l_name = input("What is your last name? ")
#     name=print(f_name.capitalize() + " " + l_name.capitalize())
#     return name
# format_name()
f_name = input("What is your first name? ") 
l_name = input("What is your last name? ")
def format_name(f_name,l_name):
    name=(f_name+" "+l_name).title()
    print(f"Your name is {name}")
    return name
print(format_name(f_name,l_name))