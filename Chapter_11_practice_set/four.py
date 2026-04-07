class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show(self):
        print(f"Complex number {self.real} + {self.img}i")
    #overloading + and * operator
    def __add__(self,c2):
        real = self.real + c2.real
        img = self.img + c2.img
        return Complex(real, img)

    # Overloading *
    def __mul__(self, c2):
        real = self.real * c2.real - self.img * c2.img
        img = self.real * c2.img + self.img * c2.real
        return Complex(real, img)


c1 = Complex(3, 5)
c2 = Complex(5, 8)

c1.show()
c2.show()

c3 = c1 + c2
c3.show()

c4 = c1 * c2
c4.show()

