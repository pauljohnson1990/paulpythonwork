pattern="ABACCDC"

#print first recursive character

char_count={}
rec_char=[] #a list for recursive character

for char in pattern:
    if char in char_count:
        rec_char.append(char)
        char_count[char]+=1
    else:
       char_count[char]=1
print(rec_char[1],"Second recursive")
print(char_count)
# word count
# first recursive character
# second recursive character
# most resursive character
high=0
most=""
#list- max, sum, min,sorted
# for char in char_count:
#     if char_count[char]>high:
#         high=char_count[char]
#         most=char
# print(most)
#iterating dictionary

for k,v in char_count.items():
    print(k,v)
person=[
    ["ram",32],
    ["rav",55],
    ["raj",44],
    ["akhil",18]
]
print(sorted(person,key=lambda p:p[1],reverse=True))
wc_list=char_count.items() #the items are changed to a tuple
print(sorted(wc_list,key=lambda item:item[1],reverse=True))
print(max(wc_list,key=lambda l:l[1]))
print(max(char_count.items(),key=lambda i:i[1]))
print(min(char_count.items(),key=lambda m:m[1]))
print(char_count.items())