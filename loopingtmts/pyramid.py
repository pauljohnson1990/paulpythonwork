num=8
#pg1
#         *
#     *   *    *
#  *    *    *    *
for row in range(0,num):
    for col in range(0,num):
        if(col>=num-row):
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
#pg1 another way
for row in range(1,5):
    for space in range(1,5-row):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end=" ")
    print()

#pg2
for row in range(0,num):
    for col in range(0,num+row):
        if(col==num-row-1 or col==num+row-1 or row==num-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
#pg2 another way
for row in range(1,5)
    