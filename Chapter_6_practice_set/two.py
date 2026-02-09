m1 = float(input("enter the marks of subject 1"))
m2 = float(input("enter the marks of subject 2"))
m3 = float(input("enter the marks of subject 3"))

total_percent = ((m1+m2+m3)/300)*100
m1_percent , m2_percent , m3_percent = (m1,m2,m3)

if total_percent >= 40 and m1_percent >=33 and m2_percent >=33 and m3_percent >=33 :
    print("pass")
else :
    print("fail")