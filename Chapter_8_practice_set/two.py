def cel_to_farhen(c):
    result = (c * (9/5)) + 32
    return result

celsius = float(input("enter temperature in celsius"))

result = cel_to_farhen(celsius)
print(f"temperature in farhenait is {result}")