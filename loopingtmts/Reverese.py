num=123
# rev=0
# while num!=0:
#     rev=rev*10+num%10
#     num=num//10
#
#
# print(rev)
res=""
while num!=0:
    lastdigit=num%10
    res=res+str(lastdigit)
    num=num//10
print(res)

