class Calculator :
    def __init__(self,num):
        self.num= num
    @staticmethod
    def greet():
        print("hello user,how are you?")
    def getCube(self):
        result = self.num**3
        return result
    def getSquare(self):
        result = self.num**2
        return result
    def getSquareRoot(self):
        result = self.num**0.5
        return result
    
num1 = Calculator(20)
num1.greet()
square = num1.getSquare()
cube= num1.getCube()
squareroot = num1.getSquareRoot()
print(f"square of {num1.num} is : {square}")
print(f"cube of {num1.num} is : {cube}")
print(f"squareroot of {num1.num} is : {squareroot}")