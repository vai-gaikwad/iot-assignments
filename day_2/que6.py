num = int(input("Enter your number :"))

def factorial(nm):
    number=nm
    fact=1
    while number>=1:
        fact=fact*number
        number=number-1
    return fact

fct=factorial(num)
print(f"factorial of {num} is {fct}")