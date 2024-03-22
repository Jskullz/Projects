capasity=int(input("What is the capasity of the bus? "))
on=int(input("How many people are on the bus? "))
wait=int(input("How many people are waiting to get on the bus? "))

def enough(cap, on, wait):
    if on + wait <= cap:
        return print("There is enough space for everyone.")
    else:
        people=(on + wait) - cap
        if people == 1:
            return print(f"{people} person needs to wait for the next bus.")
        else:
            return print(f"{people} people need to wait for the next bus.")
enough(capasity, on, wait)

