#pg1
# num1=15
# num2=35
# hcf=1
# limit= num1 if num1<num2 else num2
# print(limit)
# limit=min(num1,num2)
# print(limit)
# for i in range(2,(num1+1)):
#     if(num1%i==0 and num2%i==0):
#         hcf=i
# print(f"hcf {hcf}")

#pg2
num1=15
num2=15
num3=45
limit=0
hcf=1
if num1<num2 and num1<num3:
    limit=num1
elif num2<num1 and num2<num3:
    limit=num2
elif num3<num2 and num3<num1:
    limit=num3
for i in range(2,limit+1):
    if num1%i==0 and num2%i==0 and num3==0:
        hcf=i
print(hcf)