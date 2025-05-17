class animal:
    def __init__ (self,name,species):
        self.name=name
        self.species=species

    def showdetail(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")
class dog:
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed
    
    def showdetail(self):
        animal.showdetail(self)
        print(f"breed: {self.breed}")

class goldenretriver:
    def __init__(self,name,colour):
        dog.__init__(self,name,breed="goldenretriver")
        self.colour=colour

    def showdetail(self):
        dog.showdetail(self)
        print(f"colour:{self.colour}")

o=goldenretriver("tommy","red")
o.showdetail()
