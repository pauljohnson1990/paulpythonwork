mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
#q1 no of mobiles
# print(f"Total number of mobiles {len(mobiles)}")
# #out of stock
# out_of_stk=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stk)
# # q2 total stock
# count=0
# available_stk=[mob[-1] for mob in mobiles]
# print(sum(available_stk))
# for sub_lst in mobiles:
#     count+=sub_lst[6]
# print(count)
# q3 pritn mobiles available in range 20k to 30k
# mob_range=[mb for mb in mobiles if mb[4]>20000 and mb[4]<30000]
# mb_gt= [mb for mb in mobiles if mb[4] in range(20000,30000)]
# print(mob_range)
# # q4 print all 5g phone
# fiveg_phone=[mb for mb in mobiles if mb[2]=="5g"]
# print(fiveg_phone)
# # q5 print samsung mobiles
# samsung_mob=[mb for mb in mobiles if mb[5]=="samsung"]
# print(samsung_mob)
# # q6 print costly mobile
#
# max=0
# costly=[]
# for mb in mobiles:
#     if mb[4]>max:
#         costly=mb
#         max=mb[4]
# print(costly)
costly_pro= max(mobiles,key=lambda mob:mob[4])
print(costly_pro)
#
# max_price= max(mob[4] for mob in mobile)
# # q7 prin low cost mobiles
# low_cost=[mb for mb in mobiles if mb[4]<30000]
# print(f"low cost mobile {low_cost}")
# # q8 print all mobiles having stock >10
# stk_gtten=[mb for mb in mobiles if mb[6]>10]
# print(stk_gtten)
# # q9 count of mobiles having dispaly amoled
# count=0
# for mb in mobiles:
#     if mb[3]=="AMOLED":
#         count+=1
# print(count)
# q10 sort mobiles based on price oredr by desc
mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles)

# q11 sort mobiles based on avl stock order by desc
mobiles.sort(reverse=True,key=lambda mob:mob[-1])
print(mobiles)
# q12 is there any mobile available at rs 10000
ten_tsnd=[mob[4]==10000 for mb in mobiles if mb[4]==10000]
print("available" if True in ten_tsnd else "not available")
# q12 list all mobiles having same price

