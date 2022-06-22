account={"account_no":1000,"opening_date":"12-10-2022","type":"savings","pname":"ram"}
print(account["account_no"])
print("balance" in account)
account["balance"]=5000
print(account)

account["balance"]+=1000
print(account)

print(account.get("account_no"))
print(account.get("opening_dat"))

if "nominee_name" in account:
    account["nominee_name"]= "reshma"
else:
    account["nominee_name"]="nill"
print(account)
account["nominee_name"]="reshma" if "nominee_name" in account else "nill"
print(account)

# account balance

if account["balance"]< 10000:
    account["balance"]-=100
else:
    account["balance"]+=100
print(account)

account["balance"]+=-100 if account["balance"]<10000 else 100
print(account)

mobile={
    "mobile_name":"redminote12pro",
    "display":"led",
    "price":45000,
    "ram":"6gb",
    "memory":"64gb"
}