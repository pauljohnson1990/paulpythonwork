results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]# Result is List of Dictionary
# sort results based on win
print(sorted(results,key=lambda res:res["win"],reverse=True))
#print district with minimum win%
print(min(results,key=lambda res:res["win"]))
#sort results based on A+
print(sorted(results,key=lambda res:res["A+"],reverse=True))
#print dist with low count A+
print(min(results,key=lambda res:res["A+"]))
#print total no of students got full A+
aplus=[res["A+"] for res in results]
print(sum(aplus))