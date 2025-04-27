def average(a,b):
    print("the average of :", (a+b)/2)
average(9,1)

def average(a=9,b=1):
    print("the average of :", (a+b)/2)
average()

def average(a=9,b=1):
    print("the average of :", (a+b)/2)
average(5,1)

def average(a=9,b=3):
    print("the average of :", (a+b)/2)
average(b=1)

def name(fnae,nae="kumar",lnae="singh"):
    print("hello",fnae,nae,lnae)
name("jay")

# there is no need to pass the arguments in the function definition if we are using the default values in the

def name(fnae,nae="kumar",lnae="singh"):
    print("hello",fnae,nae,lnae)
name("jay", "sonal", "singh")


def average(a=9,b=1):
    print("the average of :", (a+b)/2)
average(a=5)

average(b=9,a=21)

def average(*numbers):

    print(type(numbers))

    sum = 0
    for i in numbers:
        sum = sum + i
    print("the average is :", sum/len(numbers))

average(5,6,7,1)

def average(*numbers):

    print(type(numbers))

    sum = 0
    for i in numbers:
        sum = sum + i
    # print("the average is :", sum/len(numbers))
    return sum/len(numbers)
c=average(5,6,7,1)
print("the averae is :",c)


def average(*numbers):

    print(type(numbers))

    sum = 0
    for i in numbers:
        sum = sum + i
    # print("the average is :", sum/len(numbers))
    return 7
    return sum/len(numbers)
c=average(5,6,7,1)
print("the averae is :",c)


