class person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
    
a = person("jay kumar singh","data scientist")
b = person("vijay kumar singh","engineer")


a.info()
b.info()