s1={1,2,4,5,6,7}
s2={3,5,6,7,8,9,10}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)


j1={1,2,3,4,5,6,7,8,9,10}
j2={1,2,3,4,5,10,11,12,13,8}
j3=j1.intersection(j2)
print(j3)



j1={1,2,3,4,5,6,7,8,9,10}
j2={1,2,3,4,5,10,11,12,13,8}
j3=j1.symmetric_difference(j2)
print(j3)


j1={1,2,3,4,5,6,7,8,9,10}
j2={1,2,3,4,5,10,11,12,13,8}
j3=j1.difference(j2)
print(j3)

j1={1,2,3,4,5,6,7,8,9,10}
j2={1,2,3,4,5,10,11,12,13,8}
j3=j1.difference_update(j2)
print(j3)


j1={1,2,3,4,5,6,7,8,9,10,22,23}
j2={1,2,3,4,5,10,11,12,13,8}
print(j1.isdisjoint(j2))


j1={1,2,3,4,5,6,7,8,9,10,22,23}
j2={32,33,34,35,26}
print(j1.isdisjoint(j2))

j1={1,2,3,4,5,6,7,8,9,10,22,23}
j2={32,33,34,35,26}
print(j1.issuperset(j2))
j3={1,2,3,4,5,10,8}
print(j1.issuperset(j3))


j1={1,2,3,4,5,6,7,8,9,10,22,23}
j2={32,33,34,35,26}
print(j1.issubset(j2))
j3={1,2,3,4,5,10,8}
print(j3.issubset(j1))


jay={"delhi","Uttar_pradesh","varanasi","tokoyo"}
jay.add("Europe")
print(jay)


j1={1,2,3,4,5,6,7,8,9,10,22,23}
j2={32,33,34,35,26}
j1.update(j2)
print(j1)  # Output: {1, 2, 3, 4,}

j1={1,2,3,4,5,6,7,8,9,10,22,23}
j1.remove(23)
print(j1)  # Output: {1, 2, 3, 4,



jay={"delhi","Uttar_pradesh","varanasi","tokoyo"}
cites=jay.pop()
print(jay) 
print(cites)

jay={"delhi","Uttar_pradesh","varanasi","tokoyo"}
del jay
print (jay)  # Output: set()  # Output: set()  # Output: