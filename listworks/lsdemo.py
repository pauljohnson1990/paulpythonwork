#   list
#   set
#   tuple
#   dict

# expenses=[12000,15000,23000,34000,45000]
# # print(expenses)
# st={True,"heelo",55,"hai",False}
# #print(st)
# # for i in range(0,len(expenses)):
# #     print(expenses[i])
# for amount in expenses:
#     print(amount)
# append
lst=[40,20,10]
lst.append(50)#add 50 to the list

# if we used "." it is a method inside the list class

expenses=[10,20,13,15,16,27]
employeenames=["rahul","jimmy"]
numbers=[12,13,14,15,18,19,20]
for num in numbers:
    if(num%2==0):
        print(num)

#count of numbers between 14 to 18
count=0
for num in numbers:
    if(num>=14 and num<=18):
        count+=1
print(count)

#or pg2
count=0
for num in numbers:
    if num in range(14,19):
        count+=1
print(count)

# neg_count
# po_count
# zero_count
numbers2=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
negcount=0
pocount=0
zerocount=0
for num in numbers2:
    if(num < 0):
        negcount+=1
    elif num==0:
        zerocount+=1
    else:
        pocount+=1
print(f"positive count = {pocount}")
print(f"negative count= {negcount}")
print(f"zero count = {zerocount}")

