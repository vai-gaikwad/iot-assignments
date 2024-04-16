print("Enter marks of 3 subject  to find its average grade ")

num1=int(input("Enter subject 1 marks  : "))
num2=int(input("Enter subject 2 marks  : "))
num3=int(input("Enter subject 3 marks  : "))
sum=(num1+num2+num3)
avrg = (sum/3)
print(avrg)

#print(f"average of {num1} {num2} {num3} = {avrg}")
def grade(avg):
    if(avg>90):
        return "A"
    elif((avg>=80 and avg<=89)):
        return "B"
    elif((avg>=70 and avg<=79)):
        return "C"
    elif((avg>=60 and avg<=69)):
        return "D"
    elif(avg<=59):
        return "F"

grd =grade (avrg)
print(f"student grade is {grd} ")




