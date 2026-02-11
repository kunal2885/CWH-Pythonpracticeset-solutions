def star_print(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end=" ")
        print()

n= int(input('enter the value of n:'))
star_print(n)