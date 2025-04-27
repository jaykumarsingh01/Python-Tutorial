l=[2354,68,18,931,2,3,4,5,6,8,9,10,23,434,65,23,23,23,23,23,23,23,23,23,23,23,23,23]
print(l)

l.append(7)
print(l)

# ACCENDING ORDER LIST 

l.sort()
print(l)

# DECENDING ORDER LIST

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(23))
print(l)

print(l.count(23))
print(l)

l.insert(1,899)
print(l)

n=[500,100,1200,1300,14000,1500,20000]
k=n+l
print(k)

l.extend(n)
print(l)
