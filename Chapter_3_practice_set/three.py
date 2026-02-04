str1 = input("enter a string")
ans = str1.find("  ")
print("double space is absent" if ans == -1 else f"double spaces are present" )

#replacing double spaces with single space
str2 = str1.replace("  "," ")
print("modified string :",str2)