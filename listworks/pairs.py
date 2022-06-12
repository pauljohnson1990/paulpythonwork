lst=[2,3,4,6,5]
# sum=8
# current_sum=0
# # for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         current_sum=lst[i]+lst[j]
#         if current_sum==sum:
#             print(f"pairs {lst[i]},{lst[j]}")
#             break

#Efficient Method
element=7
low=0
upp=len(lst)-1
cur_sum=0
while low<upp:
    cur_sum=lst[low]+lst[upp]
    if cur_sum == element:
        print(f"pairs {lst[low]},{lst[upp]}")
        low+=1
    elif cur_sum>element:
        upp-=1
    else:
        low+=1

#binary Search
#Common elements in two list

