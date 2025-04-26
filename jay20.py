a=9
b=8
gmean=(a*b)/(a+b)
print(gmean)
c=8
d=7
gmean1=(c*d)/(c+d)
print(gmean1)

# this is the code for the second part of the question or say define the function 


def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isgreater(a, b):
 if(a>b):
   print("first number is greater")
 else:
   print("second number is greater or equal")

def islesser(a, b):
  pass
#first function is that:

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
isgreater(a,b)
calculateGmean(a, b)
# second function is that:
c=int(input("enter the third number:"))
d=int(input("enter the fourth number:"))

isgreater(c,d)
calculateGmean(c, d)