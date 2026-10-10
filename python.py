#task1
a=int(input())
b=int(input())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("Numbers are equal")
#task2
x=float(input())
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("this is zero")
#task3
y=int(input())
if y%2==0:
    print("even number")
else:
    print("odd number")
#task4
y=float(input())
if y<0:
    print("Invalid score")
elif y>100:
    print("Invalid score")
elif y>91:
    print("A")
elif y>81:
    print("B")
elif y>71:
    print("C")
elif y>61:
    print("D")
elif y>51:
    print("E")
else:
    print("F")
#task5
a1=float(input())
a2=float(input())
a3=float(input())
if a1>a2 and a1>a3:
    print(a1)
elif a2>a1 and a2>a3:
    print(a2)
else:
    print(a3)
#task6
b1=int(input())
b2=int(input())
operation=input()
if operation=="+":
    x=b1+b2
    print("Netice:",x)
elif operation=="-":
    x=b1-b2
    print("Netice:",x)
elif operation=="*":
    x=b1*b2
    print("Netice:",x)
elif operation=="/":
    if b2!=0:
        x=b1/b2
        print("Netice:",x)
    else:
        print("0-a bolmek olmaz")
elif operation=="%":
    if b2!=0:
        x=b1%b2
        print("Netice:",x)
    else:
        print("0-a bolmek olmaz ve qaligi tapmaq olmur")
elif operation=="**":
    x==b1**b2
    print("Netice:",x)
elif operation=="//":
    if b2!=0:
        x=b1//b2
        print("Netice:",x)
    else:
        print("0-a bolmek olmaz ve tam hisseni tapmaq olmur")
else:
    print("Invalid operation")
#task7
age=int(input())
if age>0 and age<=12:
    print("child")
elif age>=13 and age<=17:
    print("teenager")
elif age>=18 and age<=64:
    print("adult")
elif age>=65:
    print("senior")
else:
    print("invalid age")
#task8
m=int(input())
if m<100:
    print("endirim yoxdur")
elif m>=100 and m<=299:
    endirim=m*0.1
    sonraki_qiymet=m-endirim
    print(m,endirim,sonraki_qiymet)
elif m>=300 and m<499:
    endirim=m*(15/100)
    sonraki_qiymet=m-endirim
    print(m,endirim,sonraki_qiymet)
else:
    endirim=m*0.2
    sonraki_qiymet=m-endirim
    print(m,endirim,sonraki_qiymet)
#task9
c1=int(input())
c2=int(input())
c3=int(input())
if c1>c2 and c1>c3:
    boyuk=c1
    if c2>c3:
        orta=c2
        kicik=c3
    else:
        orta=c3
        kicik=c2
elif c2>c1 and c2>c3:
    boyuk=c2
    if c1>c3:
        orta=c1
        kicik=c3
    else:
        orta=c3
        kicik=c1
else:
    boyuk=c3
    if c1>c2:
        orta=c1
        kicik=c2
    else:
        orta=c2
        kicik=c1
print(kicik,orta,boyuk)
#task10
balance=1000
t=int(input())
if t==0 and t<0:
    print("invalid amount")
elif t>balance:
    print("insufficient balance")
else:
    u=balance-t
    print(u)
#task11
i=int(input())
if i>=0 and i<=100:
    p=i*0.08
    print(i,0.08,p)
elif i>=101 and i<=300:
    p=i*0.12
    print(i,0.12,p)
elif i>300:
    p=i*0.15
    print(i,0.15,p)
else:
    print("invalid input")
#task12
h=2
r=int(input())
if r>=0 and r<=5:
    mesafehaqqi=r*0.7
    umumimebleg=h+mesafehaqqi
    print(h,mesafehaqqi,umumimebleg)
elif r>5 and r<=15:
    mesafehaqqi=r*0.6
    umumimebleg=h+mesafehaqqi
    print(h,mesafehaqqi,umumimebleg)
else:
    mesafehaqqi=r*0.5
    umumimebleg=h+mesafehaqqi
    print(h,mesafehaqqi,umumimebleg)
#task13
yas=int(input())
maas=float(input())
kredit=float(input())
if yas<18:
    if maas<500:
        if kredit>maas*10:
            print("reject the loan")
        else:
            print("approve the loan")
    else:
        print("approve the loan")
else:
    print("approve the loan")
#task14
A=float(input())
B=Float(input())
C=float(input())
if A+B>C:
    if A+C>B:
        if B+C>A:
            if A==B:
                if B==C:
                    print("equilateral")
                else:
                    print("isosceles")
            elif B==C:
                print("isosceles")
            elif A==C:
                print("isosceles")
            else:
                print("scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")
#task15
ibali=float(input())
mbali=float(input())
yas=int(input())
if yas>=16 and ibali>0 and ibali<=700 and mbali>0 and mbali<=100:
    if ibali>=600:
        print("scolarship")
    elif ibali>450 and ibali<=599:
        print("Accepted")
    elif ibali>300 and ibali<=449 and mbali>=80:
         print("accepted")
    elif ibali>300 and ibali<=449 and mbali<80:
        print("rejected")
    else:
        print("rejected")
else:
    print("Rejected")