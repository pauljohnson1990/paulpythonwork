
# lst=[10,10,1,12,13,14,15,16,16,16]
# st=set(lst)
# print(st)
# print(dir(set))
st1={1,2,3,4,5}
st2={10,11,12,2,3}
st1.add(10)
print(st1)
union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

diff_set=st1.difference(st2)
print(diff_set)

st3={100,200,300}
st1.update(st3)
print(st1)

students=["ram","ravi","hari","tom","nikhil","jain","john"]
passed_students=["ravi","hari","tom"]
failed_students=set(students).difference(set(passed_students))
print(failed_students)