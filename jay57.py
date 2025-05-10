class person:
    name="jay kuar singh"
    occupation="data scientist"
    networth=10

    def info(self):
        print(f"{self.name} is a {self.occupation} and there networth is {self.networth}" )


a=person()
c=person()
d=person()
e=person()

a.name="sonal singh"
a.occupation="engineer"
a.networth=11

c.name="vijay kumar singh"
c.occupation="ai engineer"
c.networth=12


d.name="sunil singh"
d.occupation="lawyer"
d.networth=13

a.info()
c.info()
d.info()
e.info()
