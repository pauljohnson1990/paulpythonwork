lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
#print all numbers greater than 16
flt_lst=[num for sub_lst in lst for num in sub_lst]
print(flt_lst)
for i in range(0,len(flt_lst)):
    if flt_lst[i]>25:
        flt_lst[i]+=1
    elif flt_lst[i]<25:
        flt_lst[i]-=1
print(flt_lst)
maped_lst=[num+1 if num>25 else num-1 for num in flt_lst] #mapping
print(maped_lst)
# num>25 num-1 else num+1

# for sub_ls in lst:
#     for num in sub_ls:
#         if num>16:
#             print(num)
# print(lst)
# print(max(lst)[1])
#
# flatten_lst=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_lst.append(num)
# print(flatten_lst)
# print(max(flatten_lst))
#
#
# # List Comprehension
# flt_lst=[num for sub_lst in lst for num in sub_lst]
# print(flt_lst)
#     #num greater than 16
# num_gt_sixt=[num for num in flt_lst if num>16]
# print(num_gt_sixt)
# odd_num=[num for num in flt_lst if num%2!=0]
# print(odd_num)