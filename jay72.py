class employee:
    def __init__(self , name , id):
        self.name = name
        self.id=id
    

class programmer(employee):
    def __init__(self, name, id, lan):
        super().__init__(name, id)
        self.lan=lan
    

jay=employee("jay das","421")
vijay=programmer("vijay das","2345","python")

print(vijay.name)
print(vijay.id)
print(vijay.lan)