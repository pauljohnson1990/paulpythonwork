#NESTED FOR LOOPS
# 1234
# 1234
# 1234
# for j in range(1,4):
#     pattern=""
#     for i in range(1,5):
#         pattern=pattern+str(i)
#         i+=1
#     print(pattern)
#     j+=1
# pg2
# for row in range(1, 5):
#     for col in range(1, 5):
#         print(col, end="")
#     print()

#pg3
#1 1 1
#2 2 2
#3 3 3
#4 4 4
# for row in range(1,5):
#     for col in range(1,5):
#         print(row,end="")
#     print()

#pg3
#1
#1 2
#1 2 3
#1 2 3 4
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()

#pg4
#1
#2  2
#3  3   3
#4  4   4
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()

#pg 5
#   #   #   #
#   #   #
#   #
#
for row in range(1,5):
    for col in range(5,row,-1):
        print("#",end="\t")
    print()
