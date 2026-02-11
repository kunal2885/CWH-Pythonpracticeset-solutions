def find_greatest(a,b,c):
    if a > b and a > c :
        print(f"a : {a} is largest number")
    elif b > a and b > c :
        print(f" b : {b} is largest number")
    else :
        print(f" c : {c} is largest number")
    
num1 = eval(input("enter first number"))
num2 = eval(input("enter second number"))
num3 = eval(input("enter third number"))

find_greatest(num1,num2,num3)