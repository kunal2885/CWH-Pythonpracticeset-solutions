class Vector_2d:
    def __init__(self,i,j):
        self.i= i
        self.j= j
    
class Vector_3d(Vector_2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
v1 = Vector_3d(3,4,5)
v1.show()
print(v1.i,v1.j)

