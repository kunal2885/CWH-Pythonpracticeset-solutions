a= float(input("enter the first number"))
b= float(input("enter the second number"))
c= float(input("enter the third number"))
d= float(input("enter fourth number"))

if a > b and a > c and a > d :
    print("a is largest number")
elif b > a and b > c and b > d :
    print("b is largest number")
elif c > a and c > b and c > d :
    print("c is largest number")
elif d > a and d > c and d > b :
    print("d is largest number")