print("To find lenght and breadth of rectangle")

len=int(input("Enter Lenght of rectancgle :"))
bre=int(input("Enter Breadth of rectancgle :"))

def area(l,b):
    ar = l * b
    print(f"Area of rectangle with lenght= {l} and breath {b} is {ar}")

def peri(l,b):
    pr = l + l + b + b
    print(f"Area of rectangle with lenght= {l} and breath {b} is {pr}")

area(len,bre)

peri(len,bre)

