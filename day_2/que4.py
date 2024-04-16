print("Enter 3 numbers to find max among them")

num1=int(input("Enter first number  : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number  : "))

def max(n1,n2,n3):
    if (n1 == n2 == n3):
        print("all numers are equal")
    elif (n1 == n2):
        if(n1 > n3):
            print("n1 is n2 are same and greather than n3")
        else:
            print("n3 is greather than n1 and n2 and n1 n2 are same")
    elif (n1 == n3):
        if(n1 > n2):
            print("n1 is n3 are same and greather than n2")
        else:
            print("n2 is greather than n1 and n3 and n1 n3 are same")
    elif (n2 == n3):
        if(n2 > n1):
            print("n2 is n3 are same and greather than n1")
        else:
            print("n1 is greather than n2 and n3 and n2 n3 are same")
    elif(n1>n2 and n1>n3):
        print("n1 is max")
    elif(n2>n1 and n2>n3):
        print("n2 is max")
    elif(n3>n2 and n3>n1):
        print("n3 is max")

max(num1,num2,num3)
