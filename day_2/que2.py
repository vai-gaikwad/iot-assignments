num=int(input("Enter your number : "))
temp1=num

up=int(temp1%10)
temp1=int(temp1/10)

tp=int(temp1%10)
temp1=int(temp1/10)

hp=int(temp1%10)
temp1=int(temp1/10)

thp=int(temp1%10)
temp1=int(temp1/10)

print(f"facce values of {num} = {thp} {hp} {tp} {up}")

print(f"num = {(thp*1000)+(hp*100)+(tp*10)+(up)} = {(thp*1000)} + {(hp*100)} + {(tp*10)} + {up}")

print(f"reverse of {num} = {(thp)+(hp*10)+(tp*100)+(up*1000)}")