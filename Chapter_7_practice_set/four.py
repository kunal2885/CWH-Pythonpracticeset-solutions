number = int(input("enter the number"))
for i in range(2,int((number/2))+1) :
    if number % i == 0:
        print('it is not a prime number')
        break
    else :
        print("it is a prime number")
        break
