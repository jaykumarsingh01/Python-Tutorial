countries = ("spain", "italy","india","england", "germany")
temp=list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)

countries=("pakistan","afganistan","bangladesh","shrilanaka")
countries2=("vitenam"," india","china")
southeastasia=countries+countries2
print(southeastasia)

j =(1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
ja=j.count(1)
print(ja)

j=(1,2,3,4,5,6,3,7,8,9,3,3,3,3,)
ja=j.index(3,12,13)
print(ja)


j =(1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
ja=len(j)
print(ja)

