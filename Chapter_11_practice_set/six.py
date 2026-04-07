class Vector:
    def __init__(self,i=0,j=0,k=0):
        self.i= i
        self.j= j
        self.k=k
    def __str__(self):
        return(f"{self.i}i + {self.j}j + {self.k}k")

v1 = Vector(2,3,4)
print(str(v1))