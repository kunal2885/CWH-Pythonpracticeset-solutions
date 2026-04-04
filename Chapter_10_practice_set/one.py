class Programmer:
    name= ""
    salary=0
    position=""
    def __init__(self,name,salary,position):
        self.name= name
        self.salary= salary
        self.position= position
    def getInfo(self):
        print(self.name,self.salary,self.position)

kunal = Programmer("kunal",45000,"Full Stack Engineer")
kushal = Programmer("kushal",35000,"Business Analyst")

kunal.getInfo()
Programmer.getInfo(kushal)