num=9
flag=1
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        break
if(i==num-1):
    print("Prime")

