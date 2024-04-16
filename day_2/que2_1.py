num=int(input("Enter your number :"))
temp2=num
nd=0

def digitcount(num):
    temp1=num
    nd=0
    #print(f"temp = {temp1}")
    while temp1/10 != 0:
        nd=nd+1
       # print(f"nd = {nd}")
        temp1=int(temp1/10)
        #print(f"temp = {temp1}")
        #print(f" your number ={num} contains {nd} digits in it")
    
    return nd


nid = digitcount(num)
print(f"numer {num} contains {nid} digits in it")

li = []

for i in range(0,nid):
    digit=temp2%10
    temp2=int(temp2/10)
    li.append(digit)

print(li)

for j in range(0,nid):
    print(li[j], end=" ")






