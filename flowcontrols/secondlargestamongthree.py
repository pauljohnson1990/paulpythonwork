num1=110
num2=750
num3=40
if(num1<num2 and num1>num3) or (num1<num3 and num1>num2):
    print("num1 is the Second largest")
elif(num2<num1 and num2>num3) or (num2<num3 and num2>num1):
    print("num2 is the second largest")
elif(num3<num1 and num3>num2)or (num3<num2 and num3>num1):
    print("num3 is the second largest")
elif num3==num2 and num2==num1:
    print("all numbers are same")