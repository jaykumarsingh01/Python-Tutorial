class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f"the employee is:{self.id} and there name is {self.name} ")


class programer(employee):
    def showlan():
        print("this is use python lan")

e1=employee("jay kumar singh",1)
e1.showdetails()
e2=employee("vijay kumar singh",23)
e2.showdetails()