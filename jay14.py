a=int(input("enter your age :"))
print("your age is :",a)
print(a>18)
print(a<18)
print(a<=18)
print(a>=18)
print(a!=18)
if(a>=18):
    print("you can drive ")
else:
    print("you cannnot drive")

applePrice=210
budget=200
if(applePrice<=budget):
     print("alexa you can add 1 kg apple to yhe my cart")
else:
       print("alexa you can't add 1 kg apple in the my cart")

num=int(input("enter your value : "))
if(num<0):
 print("number is negative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("number is special")
else:
    print("number is postive")

b=int(input("enter the value: "))
if(b<0):
    print("number is negative")
elif(b>0):
    if(b<=10):
        print("number is between 1-10")
    elif(b>=11 and b<=20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
  