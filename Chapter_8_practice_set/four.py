def sum(n):
    if n == 1 :
        return 1
    elif n == 0 :
        return 0
    else:
        return n + sum(n-1)
    
num = int(input("enter the value of n: "))
result = sum(num)
print(f"sum of first {num} natural numbers is : {result}")