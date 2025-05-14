class employee:
    def __init__(self, name ,salary):
        self.name=name
        self.salary=salary
    

e1=employee("jay ", 12000)
print(e1.name)
print(e1.salary)

string="vijay-12000"
e2=employee(string.split("-")[0],string.split("-")[1])
print(e2.name)   
print(e2.salary)   