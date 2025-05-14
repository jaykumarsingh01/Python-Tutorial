x=[1,2,3,4,5,6,7,8,9,]
print(dir(x))


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1

p=person("jay",21)
print(p.__dict__)
        


print(help(person))



x=(1,2,3)
y=x
y+=(4,5)
print(x)