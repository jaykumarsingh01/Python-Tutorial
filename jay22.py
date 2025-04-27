print("In the list you can add int , float, str, bool, list etc")

# no need to add the print string

list=[1,2,3,4,5,6,7,8,9,10,"JAY KUMAR SINGH", True]
print(list)
print((type)(list))
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])
print(list[9])
print(list[10])
print(list[11])

print("HERE IS THE NEGATIVE INDEXING OF THAT : ")

print(list[-3])
print(list[len(list)-3])

print("NOW THERE IS CHECK THE ITE IS PRESENT OR NOT: ")
 
if 7 in list:
    print("there is present: ")
else:
    print("there is not present: ")

if 12 in list:
    print("there is present: ")
else:
    print("there is not present: ")
    
if "jay kumar singh" in list:
    print("there is present: ")
else:
    print("there is not present: ")

if "7" in list:
    print("there is present: ")
else:
    print("there is not present: ")

if "JAY" in "JAY KUMAR SINGH":
    print("there is present: ")
else:
    print("there is not present: ")

# if you print all list of item then:

print(list)
print(list[1:-1])

# # if you need to jump the index 

print(list[1:4:2])

# LIST COPREHNSION
 
print("LIST COPREHNSION")

lst=[i for i in range(11)]
print(lst)

lst=[i*i for i in range(100)]
print(lst)
print("USING THE LOOP OF THAT: ")

lst=[i for i in range(100) if i%2==0]
print(lst)