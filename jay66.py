class employee:
    def __init__(self,name):
        self.name = name 
        self.raise_amount=0.02
    def showdetail(self):
        print(f"the name of employee is {self.name} and the raise amount is {self.raise_amount}")
    


emp1=employee("jay")
emp1.raise_amount=0.3
emp1.showdetail()

emp2=employee("vijay")

emp2.showdetail()