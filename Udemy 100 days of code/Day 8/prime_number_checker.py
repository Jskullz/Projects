def prime_number(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
number=int(input("Enter a number: "))
prime_number(number)
