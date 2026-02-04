marks =[]
i= 1
while i<7 :
    mark = float(input("enter the marks of the student"))
    marks.append(mark)
    i= i+1

marks.sort()
print(marks)