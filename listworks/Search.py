lst1=[10,11,12,13,14,15,20,21,22,34]
lst2=[11,12,20,21]
element=32
lst1.sort()
flag=0
low=0
upp=len(lst1)
while low<upp and lst1[upp-1]>=element:
    mid=(upp+low)//2
    if lst1[mid]== element:
        flag=mid
        break
    elif lst1[mid]<element:
        low=mid
    elif lst1[mid]>element:
        upp=mid
print(f"element Found at {flag+1} position" if flag>0 else "element not found")