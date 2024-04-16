def factorial(nm):
    number=nm
    fact=1
    while number>=1:
        fact=fact*number
        number=number-1
    return fact

for j in range (1, 11):
    fct=factorial(j)
    print(f"factorial of {j} is {fct}")