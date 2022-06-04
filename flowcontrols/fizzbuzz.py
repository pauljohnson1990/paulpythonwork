num=8
# if(num%3==0):
#     print("fizz")
# if(num%5==0):
#     print("bizz")
# if(num%15==0):
#     print("fizzbizz")
# if(num%15!=0):
#     if(num%3==0):
#         print("fizz")
#     else:
#         if(num%5==0):
#             print("bizz")
#         else:
#             print(f"{num} not divisible by either 3,5 or 15")
# else:
#     print("fizzbizz")
num =30
res=""
if num%3==0:
    res+="fizz"
if num%5==0:
    res+="buzz"
print(res)
