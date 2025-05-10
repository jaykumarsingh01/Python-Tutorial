def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,3,4,5,6,7,8,9]
new=[]
for item in l:
    new.append(cube(item))




new=list(map(cube,l))
print(new)




# FILTER
def filter_function(a):
    return a>2
newl=list(filter(filter_function,l))
print(newl)



#reduce
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]

def su(x,y):
    return x+y
sum=reduce(su,numbers)
print(sum)