def greet(fx):
    def mfx(*args,**kwars):
        print("Good Morning everyone")
        fx(*args,**kwars)
        print("thanks for using this function")

    return mfx
@greet
def jay():
        print("har har mahadev")

@greet
def add(a,b):
 print(a+b)


jay()
add(1,2)
