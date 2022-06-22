accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]
all_transaction=[ac["transactions"] for ac in accounts ]
transaction=[trans for tlist in all_transaction for trans in tlist]
print(transaction)

#print details of ac 1002

# for ac in accounts:
#     if ac["acno"]==1002:
#         transactions=ac.pop("transactions")
#         print(ac)
# print(transactions)
# ac_details=[ac for ac in accounts if ac["acno"]==1002]
# print(ac_details)

#q2 print savings type account details
savings_type=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
print(savings_type)

#q3 Sort Accounts bases on balance
# sorted_acc=sorted(accounts,key=lambda bal:bal["balance"],reverse=True)
# print(sorted_acc)
accounts.sort(reverse=True,key=lambda ac:ac["balance"])
print(accounts)
#q4 print all phone Pay transactions
print()
print("print all phone Pay transactions")
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["method"]=="phone-pay":
#             print(ac["acno"],tr)
phonepay_tr=[tr for tr in transaction if tr["method"]=="phone-pay"]
print(phonepay_tr)
#print all transactions where transaction amount >500
print()
print("print all transactions where transaction amount >500")
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["amount"]>500:
#             print(ac["acno"],tr)
abovefivehundred_tr=[tr for tr in transaction if tr["amount"]>500]
print(abovefivehundred_tr)
#q5 credit transactions of 1002
print()
print("credit transactions of 1002")
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["to"]==1002:
#             print(ac["acno"],tr)
crdtr_1002=[tr for tr in transaction if tr["to"]==1002]
print(crdtr_1002)
#q6 aggregate transactions based on payment methods
print()
print("All Transaction")
ag_met={}
for tr in transaction:
    if tr["method"] in ag_met:
        ag_met[tr["method"]]+=tr["amount"]
    else:
        ag_met[tr["method"]]=tr["amount"]
print(ag_met)
#q6 Max of the aggregate trans
print(max(ag_met.items(),key=lambda ite:ite[1]))