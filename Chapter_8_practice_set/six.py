def inch_to_cm(inch_value):
    result = inch_value * 2.54
    return result

value = eval(input("enter value in inches"))
print(inch_to_cm(value))