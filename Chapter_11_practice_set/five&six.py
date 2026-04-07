class Vector:
    def __init__(self,i=0,j=0,k=0):
        self.i= i
        self.j= j
        self.k=k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
    def __add__(self,v2):
        i= self.i + v2.i
        j= self.j + v2.j
        k= self.k + v2.k
        return Vector(i,j,k)
    def __mul__(self,v2):
        dot_product = self.i * v2.i +  self.j * v2.j + self.k * v2.k
        return dot_product
    def __len__(self):
        dimension = 0
        if(self.i != 0):
            dimension+= 1
        if(self.j != 0):
            dimension+= 1
        if(self.k != 0):
            dimension+= 1
        return dimension
            



v1 = Vector(2,3,4)
v2 = Vector(5,6,7)
v1.show()
v2.show()
v3= v1+v2
v3.show()
print(v1*v2)
print(len(v2))
        
        