num=4
# i=0
# numnext=0
# sum=0
# while i<num:
#     numnext=10**i + numnext
#     sum=sum+ numnext*num
#     i+=1
# print(f"sum {sum}")

#logic2
i=1
pattern=""
sum=0
while i<=num:
    pattern=pattern + str(num)
    sum=sum+ int(pattern)
    i+=1
print(sum)