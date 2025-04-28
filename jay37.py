try:
    l=[1,5,6,7]
    i=int(input("enter the value"))
    print(l[i])
except:
    print("some error occured")


def func1():

 try:
    l=[1,5,6,7]
    i=int(input("enter the value"))
    print(l[i])
    return 1
 except:
    print("some error occured")
    return 0
 
 finally:
   print("i a always  executed")




x=func1()
print(x) 
 
